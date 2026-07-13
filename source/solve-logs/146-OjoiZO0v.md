# Solve log: 学舌

- Puzzle ID: `OjoiZO0v`
- Owner: `codex-sub-b-20260712`
- Status: correct
- Incorrect submissions: 0

## Observations

- Flavor is Mandarin characters imitating Cantonese: `乜嘢，你发鹅浦东发不包尊？` approximates `咩嘢，你话我普通话唔标准？`. Tags also explicitly include 方言, 音乐, 密码.
- The image has four Cantonese romanizations beside pitch/note positions: `lou`, `gung`, `sin`, `put`.
- Reading the note positions as tone numbers supplies `lou5`, `gung1`, `sin3`, and `put3`.
- The romanizations are horizontally staggered. Sorting by their x-coordinates, rather than the vertical panel order, gives `lou5 gung1 put3 sin3`.
- This decodes to `老公拨扇`, a Cantonese/Hakka two-part saying. Its conventional punchline is `凄凉`, punning on `妻凉` (the husband fans, so the wife is cool/cold).
- The third hint title `里程碑之后` is consistent with treating `老公拨扇` as a milestone and then completing the saying.

## Candidate ranking

1. `凄凉` - conventional written punchline to `老公拨扇`, and semantically contrasts the speaker's claim of melodious oriole-like speech.
2. `妻凉` - literal pun expansion, but dictionaries and normal usage list the saying as `凄凉`.

## Submissions

- `凄凉` - correct at `2026-07-12T20:42:02Z`; conventional punchline to `老公拨扇`.

## Stopping criteria

- Submit the conventional saying punchline first.
- Stop after 20 incorrect submissions, or classify `cannot_do` earlier if later evidence cannot distinguish candidates.
