# LiikuNyt: demo and submission guide

Jonathan & Josh | STUHI Tampere | 25 October 2026

## What you have

A working, bilingual sports-discovery website with an interactive Tampere map, room-level filters, a Time Machine, travel-aware matching, workout plans, favorites, comparison, share links and a simulated booking-change demonstration.

**Say this clearly:** “The facilities are real. Every availability interval is sample data. We have not connected to live Timmi bookings.”

The app answers the challenge by connecting activity, time, place and the practical next steps. It does not reserve facilities or sell tickets. “Free slot” means an unoccupied slot, not a free ticket.

## Before presenting

1. Open the deployed link supplied with the handoff on the laptop you will present from.
2. Open **Demo-ohjaus / Demo controls → Palauta demo / Reset demo**. This restores 25 October 2026 at 17:00, clears the saved plan and local simulated changes, and keeps favorites and language.
3. Use FI/EN to choose your presentation language. Finnish is the default for a fresh browser.
4. Remove any saved hearts if you want the exact baseline ranking below. Favorites affect ranking; Reset demo deliberately preserves them.
5. Click **Löydä minulle treeni / Find my workout**. Expect two gyms: Hervanta and Tesoman jäähalli. Starting point: Keskustori. Travel: cycling. Minimum workout: 30 minutes.
6. Keep the official Timmi page ready in another tab. Do not spend your presentation logging in or buying a ticket.
7. Rehearse once together. Jonathan speaks first; Josh operates the app and continues the explanation.

## Reliable 90-second walkthrough

| Time | Action | What to explain |
| --- | --- | --- |
| 0–15 s | Click Find my workout. Show the two gym results at 17:00. | “I want to exercise. Which place fits my time and journey?” Point out the sample-data label. |
| 15–30 s | Select Hervanta on the map or by its card title. Click Plan my workout. | “The plan combines the room, example window and estimated journey.” From Keskustori the cycling estimate is 37 minutes, leaving 83 minutes in the 16:00–19:00 example window. |
| 30–40 s | Point to Check in Timmi, directions and ticket information. | “Check the official availability before buying. The ticket does not reserve the room.” Timmi opens its entry page. |
| 40–60 s | In the plan, open Demo controls. Keep Hilkka selected. Click Mark occupied in demo, then My plan. | “This is a simulated change. The old plan no longer fits, and Tesoma is offered as an alternative.” |
| 60–75 s | Close the plan. Move the Time Machine to 15:00, then 19:00. | “The same logic recalculates the list, map and recommendations as time changes.” Do not promise specific real bookings. |
| 75–90 s | Reset demo. Optionally type “Haluan kuntosalille Hervannassa klo 17”. | “A simple supported sentence updates the same filters. It is a rule-based parser, not a general AI chatbot.” |

At 19:00 the Hilkka example becomes occupied; this is deliberately scripted in the dataset. Other sample statuses also change with time. If a demo control seems to have no effect, check that you selected a currently free interval on the demonstration date.

For a faster 60-second version, omit the natural-language search and spend more time on the changed-plan warning. Show the result before explaining implementation details.

## Two-minute pitch

Approximately 220 spoken words, leaving room for a few clicks. Rehearse for your speaking speed.

### Jonathan, opening and demo introduction

“It is five o’clock. You want to work out, but first you need to find a suitable place, check the time and work out how to get there. That can be enough effort to make you stay home.

We built LiikuNyt to turn that question into a practical plan.

Choose an activity, a starting point and a time. LiikuNyt brings matching rooms onto one map and helps you compare the journey.

These are real Tampere facilities. The booking intervals are clearly labeled examples. We do not have a live Timmi connection.

Let’s look for a gym at five. Here are two options, and here is our suggested plan.”

### Josh, demonstration and close

“The plan shows the room, the example time window and an estimated journey. It also links to Timmi for verification and the city’s ticket information.

Now I’ll mark this example occupied. The original plan no longer fits, and LiikuNyt offers another option. Moving the time slider updates the same results and map.

Our matching logic is transparent. It checks the activity, example availability and time left after travel before ranking suitable choices. Walking and cycling times are estimates. Transit needs checking in the journey planner.

The next step is authorized booking data and testing with residents. Our goal is simple: less time searching, more time moving.”

If asked about AI assistance, answer directly: “We used AI coding assistance to build this prototype. We can explain its data model, matching rules, demo behavior and limitations.” Only add claims about your personal contribution that are true.

## Ten questions judges may ask

1. **Why is this useful?** It puts the activity, room, time and journey into one decision. The goal is to reduce the work between wanting to exercise and knowing what to check next. We have not yet measured behavior change.
2. **What is innovative?** The useful combination is time-sensitive room discovery with travel feasibility and a plan that responds to changes. The Time Machine makes those relationships visible. We are not claiming to have invented maps or booking systems.
3. **Why are bookings simulated?** We have no confirmed authorized Timmi data feed. The brief permits examples, so we built a deterministic dataset and label it throughout instead of presenting guesses as live availability.
4. **How do you handle unreliable information?** Real facility records and fictional slots are separate. Every facility has sources, unknown season dates exclude Hall A, and the app directs users to verify current information before purchase. Live data would additionally need timestamps, expiry rules and outage handling.
5. **How accurate are the map and travel times?** Markers use LIPAS facility coordinates. The map is a simplified local geographic backdrop. Distances are straight-line; walk/cycle times use explicitly stated assumptions. Transit times are not calculated. Directions open an external planner for checking the actual route.
6. **Will it scale to more cities?** The facilities, rooms and intervals are structured separately, so another city can use the same model. Production would need authorized data adapters, caching, room-ID mapping and a map/routing service with appropriate coverage. Large-scale performance has not been tested.
7. **What about privacy?** The app has no accounts or analytics. Preferences and plans stay in browser storage. Precise GPS is kept only in memory and removed from stored/shared plans. Opening Google Maps sends trip coordinates to that provider; hosting and external services have their own policies.
8. **What would make it production-ready?** Authorized current availability, exceptional opening hours, seasonal rules, freshness/error handling, realistic routing, accessibility and security review, monitoring, and tests with venue staff and residents.
9. **Why not use Timmi directly?** Timmi remains the official verification destination. LiikuNyt adds a resident-facing discovery and journey layer across participating facilities. We have not proved it is faster than Timmi in a usability study.
10. **What did you actually build?** A working browser application: data model, filters, interactive map, deterministic ranking, plan/share logic, demo updates, bilingual interface, comparison and favorites. The parser is rule-based. The map uses Leaflet and public geographic data. No production booking backend or payment system was built.

## Test report

The continuation run executed **16 automated tests: 16 passed, 0 failed**. These cover facility/room structure, slot intervals, default gym matches, hard filters, occupied-slot rejection, time-dependent changes, seasonal exclusion, distance estimates, transit uncertainty, ranking, bilingual query parsing, directions URLs, share-link restoration, Helsinki time on the daylight-saving transition date, saved-plan trip isolation, GPS removal and valid local overrides.

Direct browser checks in this continuation:

- Initial load, local basemap and eight facility markers.
- 17:00 gym quick start, Hervanta plan, simulation-induced invalidation and Tesoma alternative.
- Demo reset and supported Finnish natural-language search.
- English labels, results and plan explanations.
- Time slider changes and non-demo-date empty state.
- Two-facility comparison and marker selection with the correct facility details.
- Mobile iframe layouts at 375 and 430 pixels; no horizontal body overflow in the measured layouts.
- Geolocation denied by iframe policy: informative message, manual starting area remains usable.
- Official Timmi, ticket and Google Maps destinations inspected in rendered links; URL construction covered by automated tests.

Earlier build-session checks reported and preserved: OpenStreetMap tile images were blocked and replaced with bundled geography; cramped mobile date/time inputs were fixed; saved/share plan origin and travel settings were isolated from later search changes. The current automated suite verifies that plan-state fix.

Verification limits: physical iPhone/Android devices, Safari, a full assistive-technology audit, live GPS acquisition, external Timmi account flows, payment, road-route accuracy, transit departures and load testing were not verified. The responsive check is a browser iframe, not a physical-device certification. Deployment status is reported with the delivered app link.

## Known limits you should be ready to explain

- Example availability exists only on 25 October 2026. A different date returns no sample results.
- There is no live Timmi integration, real booking, payment or exclusive access guarantee.
- Selecting 17:00 means departure at 17:00, not a guaranteed workout start at 17:00.
- The ranking is a heuristic. Transit results remain conditional on checking the real journey time.
- Timmi links open the entry page. No room or time is preselected.
- Google Maps links carry origin/destination/mode, but users set the intended date/time there.
- Real exceptional closures, events, prices and detailed accessibility information must be checked officially.
- Hall A has no suggested availability until its sports-season dates are confirmed.
- The page has bundled assets but no service worker, so offline reload is not guaranteed. A locally served source copy is a useful presentation backup.
- Saved preferences are per browser. Shared links contain the selected example and demo overrides, not a reservation or shared live state.

## Submission checklist

- Use the verified deployment URL delivered with this guide.
- Check the reported access status; judges need a public link or explicit access.
- Keep the source export and this guide together. The source includes README, tests, docs and the runnable `dist/` app.
- Run the demo once on your presentation laptop and phone.
- Practice the pitch with a timer; use the two-minute version above, then answer questions.
- Include the sentence “Availability is simulated; facility information comes from official sources.”
- Do not claim a partnership with Tampere or a live booking integration.
- Submit through the organizers’ actual submission form before their deadline. No hackathon submission has been sent for you.

## Sources

- [Liikkuva Tampere ticket and eligible rooms](https://www.tampere.fi/liikunta/liikuntatilojen-kayttovuorot-ja-varaaminen/liikkuva-tampere-lippu)
- [Official Timmi entry point](https://timmi.tampere.fi/WebTimmi/)
- [LIPAS sports facility data](https://www.lipas.fi/liikuntapaikat)
- [City of Tampere geographic interfaces](https://www.tampere.fi/kartta/paikkatietoaineistojen-latauspalvelut-ja-rajapinnat)

Each facility’s official information page and coordinate API link are retained in the app. See README for architecture, local startup and a realistic future integration plan.
