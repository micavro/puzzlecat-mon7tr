# LWPqNrv1 - 黑板

Owner: `chat2-root-20260712`

## Observations

- Archive completed with 12 files and one resource, with no failures.
- On the chalkboard, colored digits `1 2 3 4` align with colored letters
  `w e l l` as an example. The target has colored `1 2 3` followed by two
  apparently blank boxes, producing three visible letters and two blanks.
- Flavor says the numbers give the letters' positions in the colors.

## Reasoning

- Interpret each chalk color by its English color name and index it with the
  displayed digit:
  - Example: `WHITE[1]=W`, `RED[2]=E`, `YELLOW[3]=L`, `YELLOW[4]=L`, giving
    `WELL` exactly.
  - Target visible cells: `BLUE[1]=B`, `GREEN[2]=R`, `WHITE[3]=I`.
- The remaining target indices are naturally `4` and `5`. They are written in
  black chalk on a blackboard, so both digits and letters are invisible:
  `BLACK[4]=C`, `BLACK[5]=K`.
- The completed five-letter word is `BRICK`.

## Candidate ranking

- `BRICK` - every color/index and the invisibility gimmick are explained.

## Submissions

- `BRICK` - correct (`2026-07-12T13:07:10.282Z`).
- Total incorrect: `0 / 20`.

## Result

- `correct`: `BRICK`.

## Stopping criteria

- Resolve `correct` after an accepted, mechanism-supported answer.
- Resolve `cannot_do` if evidence cannot distinguish candidates.
- Resolve `wrong_20` after exactly 20 incorrect submissions.
