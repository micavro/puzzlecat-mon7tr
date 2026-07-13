# Solve log: cSyHRhJe

## Coordination

- Owner: `codex-sub-c-20260712`
- Title: 旅行前也要先填饱肚子呀...
- Claimed: 2026-07-12T06:51:59.708Z
- Archived successfully through `npm run work -- archive`.
- Incorrect submissions: 1
- Status: correct

## Observations

- Tags: 图寻, Hunt.
- Archive reports no separately downloaded resources; inspect embedded page content and screenshot.
- The six numbered paragraphs describe one continuous route in Singapore.
- Public reference checks identify the key names and descriptions:
  - Thian Hock Keng Temple (天福宫), whose famous plaque reads `波靖南溟`, matches paragraph 1.
  - Collyer Quay is officially a Singapore CBD road and its Chinese name is `哥烈码头`, matching paragraph 2's `...码头` road full of offices.
  - Merlion Park contains the water-spouting lion-head/fish-tail composite creature.
  - Jubilee Bridge is the pedestrian bridge immediately north of the Merlion route.
  - War Memorial Park contains the conspicuous white Civilian War Memorial columns.
  - Changi Exhibition Centre is the convention venue on Singapore's far eastern coast.
  - Loyang is a Singapore subzone served by Loyang Avenue; its name means `brass` or `tray` in Malay, exactly matching paragraph 6.

## Reasoning and candidates

- Following the stated indices gives:
  1. The wording by the green rubbish-bin icon at the temple starts with `S`.
  2. `Collyer Quay`, second letter of the final word `Quay` -> `U`.
  3. `Jubilee Bridge`, third letter -> `B`.
  4. `War Memorial Park`, first letter -> `W`.
  5. `Changi Exhibition Centre`, third letter -> `A`.
  6. `Loyang`, fourth letter from the end -> `Y`.
- Extraction: `SUBWAY`.
- The title confirms the intended double meaning: Subway provides food before taking a subway for travel.
- Candidate ranking:
  1. `SUBWAY` — overwhelming; exact six-letter extraction plus title double meaning.
  2. `SANDWICH` — thematic only and does not match the indexed letters; rejected.
- `SUBWAY` was accepted as an intermediate answer. The site message was: `加油！乘坐地铁旅行没准会更方便。`
- This directs a second stage rather than counting as an incorrect answer.
- The conspicuously unused wording in paragraph 5 places a man named `汤姆逊` (Thomson) at the city's `东岸` (East Coast). In Singapore subway context this exactly names the `Thomson-East Coast Line`.
- Second-stage ranking:
  1. `CHANGI` — exact MRT-code extraction described below.
  2. `THOMSON EAST COAST LINE` — rejected by submission; it accounts for only one paragraph's line clue, not the complete second-stage mechanism.
- The intermediate instruction means to reinterpret one line-direction phrase and one number in each paragraph as a Singapore MRT station code:
  1. `非常圆` (Circle) + 17 -> `CC17 Caldecott`.
  2. `东北` (North East) + about 6 intersections -> `NE6 Dhoby Ghaut`.
  3. `南北` (North South) + age 18 -> `NS18 Braddell`.
  4. `回到了城里` (Downtown) + the number after ten (`下个十字`) -> `DT11 Newton`.
  5. `汤姆逊` + `东岸` (Thomson-East Coast) + 28 minutes -> `TE28 Siglap`.
  6. `东张西望` (East West) + 3 miles -> `EW3 Simei`.
- Reuse the first-stage extraction indices `1, 2, 3, 1, 3, reverse 4` on these station names:
  - Caldecott[1] = C
  - Dhoby Ghaut[2] = H
  - Braddell[3] = A
  - Newton[1] = N
  - Siglap[3] = G
  - Simei[reverse 4] = I
- Final extraction: `CHANGI`.

## Submissions

- `SUBWAY` -> intermediate (not incorrect): `加油！乘坐地铁旅行没准会更方便。`
- `THOMSON EAST COAST LINE` -> incorrect. Incorrect count: 1. The direct phrase construction was insufficient and is rejected; do not enumerate alternate line-name spelling variants.
- `CHANGI` -> correct. Final incorrect count: 1.

## Stopping criteria

- Submit only candidates supported by a recovered identification/extraction mechanism.
- Stop at 20 incorrect submissions, or earlier as `cannot_do` if archived/public evidence cannot distinguish candidates.
- Stopped because `CHANGI` received a correct verdict; no further submissions are needed.
