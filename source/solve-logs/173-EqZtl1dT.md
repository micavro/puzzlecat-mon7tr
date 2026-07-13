# EqZtl1dT - 打字比赛

Owner: `chat2-root-20260712`

## Observations

- Archive completed with 12 files and no failed resources.
- The image is a blank three-row QWERTY letter keyboard with numbers at these
  physical positions: `1=F`, `2=Y`, `3=A`, `4=W`, `5=K`, `6=L`.
- The text gives `1+2 = landlord`, `3+4 = worker`, `5+6 = ?`, with answer
  enumeration `(5)`.
- Flavor text says the author became unusually fast after changing keyboards,
  pointing to an input method/layout rather than ordinary English key labels.

## Reasoning

- On the Wubi keyboard, the 25 first-level simplified characters map one-to-one
  to letter keys. The six marked positions are:
  - `F -> 地` (land)
  - `Y -> 主` (lord)
  - `A -> 工` (work)
  - `W -> 人` (person / agent suffix)
  - `K -> 中` (middle)
  - `L -> 国` (country)
- This exactly verifies both examples: `F+Y -> 地主 -> landlord`, and
  `A+W -> 工人 -> worker`.
- Therefore `K+L -> 中国`, whose five-letter English answer is `CHINA`.

## Candidate ranking

- `CHINA` - uniquely supported by the complete Wubi first-level-code mapping
  and the `(5)` enumeration.

## Submissions

- `CHINA` - correct (`2026-07-12T11:48:22.948Z`).
- Total incorrect: `0 / 20`.

## Result

- `correct`: `CHINA`.

## Stopping criteria

- Resolve `correct` after an accepted, mechanism-supported answer.
- Resolve `cannot_do` if archived evidence cannot distinguish remaining candidates.
- Resolve `wrong_20` after exactly 20 incorrect submissions.
