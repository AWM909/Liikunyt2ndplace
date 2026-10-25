"""Render an intentionally simplified local basemap from Tampere's public WFS.
Run with scratch directory containing water.json, green.json, roads.json.
Coordinates remain in their actual Web Mercator positions. Not a routing map.
"""
import json,math,sys,html
from pathlib import Path
src=Path(sys.argv[1]);dst=Path(sys.argv[2])
bounds=[23.54,61.415,23.97,61.55]
def project(p):
 x,y=p;return x,math.degrees(math.log(math.tan(math.pi/4+math.radians(y)/2)))
left,bottom=project(bounds[:2]);right,top=project(bounds[2:]);W=2400;H=round(W*(top-bottom)/(right-left))
def xy(p):
 x,y=project(p);return [(x-left)/(right-left)*W,(top-y)/(top-bottom)*H]
def simplify(points,tol):
 if len(points)<4:return points
 a,b=points[0],points[-1];dx=b[0]-a[0];dy=b[1]-a[1];d=dx*dx+dy*dy
 best=0;idx=0
 for i,p in enumerate(points[1:-1],1):
  k=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/d))if d else 0
  dist=(p[0]-a[0]-k*dx)**2+(p[1]-a[1]-k*dy)**2
  if dist>best:best=dist;idx=i
 if best>tol*tol:return simplify(points[:idx+1],tol)[:-1]+simplify(points[idx:],tol)
 return [a,b]
def path(rings):
 out=[]
 for ring in rings:
  pts=[xy(p[:2])for p in ring];pts=simplify(pts,.35)
  if len(pts)<4:continue
  out.append('M'+'L'.join(f'{p[0]:.1f},{p[1]:.1f}'for p in pts)+'Z')
 return ''.join(out)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><title>Tampere, simplified geographic backdrop from City of Tampere WFS</title><rect width="100%" height="100%" fill="#edf0e7"/>']
count={}
for name,color,stroke in [('green','#dbe5cb','none'),('water','#c8dedc','#b8d1cd'),('roads','#ffffff','#d5ddce')]:
 s=json.load(open(src/(name+'.json')));paths=[]
 for f in s['features']:
  g=f['geometry'];typ=g['type'];polys=g['coordinates']if typ=='MultiPolygon' else [g['coordinates']]if typ=='Polygon'else[]
  for p in polys:
   v=path(p)
   if v:paths.append(v)
 count[name]=len(paths);svg.append(f'<path fill="{color}" stroke="{stroke}" stroke-width="0.65" fill-rule="evenodd" d="'+''.join(paths)+'"/>')
# Labels at known facility/locality anchors; placement adjusted only for legibility.
labels=[('TAMPERE',[23.766,61.498]),('HERVANTA',[23.855,61.447]),('TESOMA',[23.628,61.5125]),('KAUPPI',[23.818,61.512]),('KAUKAJÄRVI',[23.882,61.472]),('HÄRMÄLÄ',[23.735,61.470])]
for label,pt in labels:
 x,y=xy(pt);svg.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" fill="#7b8c7d" font-family="Arial,sans-serif" font-size="{65 if label=="TAMPERE" else 48}" font-weight="600" letter-spacing="3">{html.escape(label)}</text>')
svg.append('</svg>');dst.write_text(''.join(svg));print('Rendered',count,'size',dst.stat().st_size,'bounds',bounds,'dimensions',W,H)
