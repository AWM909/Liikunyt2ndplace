# LiikuNyt

**Löydä liikuntahetkesi. Find your next workout.**

A working student prototype for the Tampere challenge: “Where can I exercise right now, and how do I get there?” Built for Jonathan and Josh's STUHI 2026 demonstration with AI coding assistance.

**All availability is simulated. No live Timmi integration exists.** Green markers identify matching examples, not confirmed available rooms. The paid, personal Liikkuva Tampere ticket does not reserve a space. Check the official service before buying.

## Run

Requires Python 3 for the local web server and Node.js 18 or newer for tests. No npm install or build step is needed.

```sh
python3 -m http.server 3000 --directory dist
```

Open http://localhost:3000. Do not double-click index.html: browsers restrict local ES module imports. On Windows, `py -m http.server 3000 --directory dist` is an alternative.

```sh
node --test tests/*.test.mjs
```

Deploy `dist/` to static hosting. The Sites deployment configuration is `.openai/hosting.json`. Use the verified app URL supplied with the handoff for the hosted version.

## Implemented

- Eight Tampere facilities and 35 individually modeled ticket-eligible rooms.
- Finnish/English interface; official facility and room names remain in Finnish.
- Interactive Leaflet map, local geographic backdrop, eight selectable markers, map/card synchronization and fit-all control.
- Activity, date, departure time, starting area, travel mode, straight-line distance and minimum workout filters.
- Deterministic Time Machine for 25 October 2026, in Helsinki wall-clock time.
- Explainable Smart Match with hard eligibility checks before ranking.
- Workout plans, route links, official Timmi entry link and city ticket guidance.
- Favorites, two/three-facility comparison and browser persistence.
- Rule-based Finnish/English search for supported activities, areas, times and travel modes.
- Local demo occupancy controls, invalidated-plan warnings and replacement suggestions.
- Share links without accounts. Exact GPS coordinates are excluded from shared and stored plans.
- Keyboard-operable controls, focus styles, reduced-motion styling and mobile layouts.

## Architecture

Buildless HTML, CSS and JavaScript ES modules. No application server, database, paid API or remote AI service is needed. Leaflet is bundled locally with its license. Search remains usable if the map module fails.

| File | Responsibility |
| --- | --- |
| `dist/data.js` | Facility facts, room eligibility, category labels, source URLs and starting areas |
| `dist/coordinate-provenance.json` | Retained LIPAS coordinate evidence |
| `dist/demo.js` | Fictional, deterministic room intervals, separate from real facility data |
| `dist/logic.js` | Filtering, distance estimates, ranking, query parsing and plan serialization |
| `dist/app.js` | UI state, dialogs, local storage and interactions |
| `dist/map.js` | Leaflet map and status markers |
| `dist/tampere-map.svg` | Simplified bundled geography, not a navigation map |
| `dist/i18n.js` | Finnish and English UI copy |
| `tests/logic.test.mjs` | Automated behavioral checks |
| `dist/qa.html` | Optional responsive iframe harness with location permission denied |
| `docs/HANDOFF.md` | Demo, pitch, judge questions, QA and limitations |

Distance is Haversine straight-line distance. Walking/cycling estimates use distance × 1.3 at 4.5/15 km/h, rounded up with a two-minute minimum. These are rough assumptions, not routed travel times. Public transport time is deliberately unknown: the app links to Google Maps instead. Users must select the intended date and time there.

Eligibility requires a matching activity, a free sample slot, the distance/favorite filters and enough time for the selected minimum workout after estimated travel. Transit results are conditional on checking journey time. Ranking favors a longer usable window, shorter travel and saved facilities. The heuristic is not scientifically validated.

## Data and attribution

Facility eligibility and ticket rules: [City of Tampere, Liikkuva Tampere ticket](https://www.tampere.fi/liikunta/liikuntatilojen-kayttovuorot-ja-varaaminen/liikkuva-tampere-lippu). Facility addresses and room classifications use each official facility page linked from `data.js`. Venue details are a dated snapshot, not continuously refreshed.

Coordinates: [Lipas.fi, University of Jyväskylä](https://www.lipas.fi/liikuntapaikat), retrieved 25 October 2026, CC BY 4.0. Individual API source URLs are retained per facility. Coordinates represent the sports facility, not a verified accessible entrance.

Map backdrop: City of Tampere [public WFS geographic data](https://www.tampere.fi/kartta/paikkatietoaineistojen-latauspalvelut-ja-rajapinnat), retrieved during the build. Water areas (2022), parks and street polygons were simplified and rendered into SVG; labels were added. It is not a route network. `scripts/make-basemap.py` can recreate it with the corresponding downloaded GeoJSON files. Those raw downloads are not required to run the app and are not part of this source export.

The A-hall sports season could not be confirmed, so A-hall appears in facility details but has no suggested intervals. Some rooms have general exercise categories; users must confirm specific sport suitability. Sunday interval endings are conservative demonstration bounds derived during source review, not a promise of opening or admission on the demo date. Event closures are not modeled.

Official verification: https://timmi.tampere.fi/WebTimmi/. The link opens the entry page, not a preselected room/time. The challenge PDF was unavailable during the original research; the supplied brief and official city pages guided the build.

## Privacy and limits

The application contains no analytics or user accounts. Favorites, language, example overrides and the plan use local storage in that browser. Precise GPS remains in memory; storing or sharing a GPS plan replaces its starting point with Keskustori and displays a warning. Opening directions deliberately sends origin/destination to Google Maps. Hosting and external services have their own request logging and privacy policies.

This is a single-day demo, not a production booking service. It has no live bookings, payments, reservations, real-time transit, road routing, accessibility audit or guaranteed offline reload. Demo changes are local, except when explicitly encoded in a shared plan URL. The broad search assistant does not understand arbitrary language.

## Path to production

Agree data access with Tampere and the booking-system provider. Introduce an authorized read-only adapter with stable facility/room IDs, Helsinki-aware timestamps, cancellations, exceptional hours and seasonal rules. Validate data contracts, track source freshness, and treat stale/unknown availability as unknown. Add secure server-side credentials, caching, error monitoring and refresh policies before presenting any live status. Then integrate a permitted routing service and test with residents and venue staff. Do not scrape or bypass Timmi access controls.
