# RkaAJFgi 【星谜002】ReReRebus — solve log

- Owner: `codex-sub-g-20260712`
- Status: correct
- Incorrect submissions: 0

## Observations

- The single image contains three rebus equations and asks for `ANS: αγβ`.
- Top: `SP` + a ring = `SPRING`. The α brace selects positions 2–4, `PRI`.
- Lower left: `S` on top of `G` = `S ON G` = `SONG`. The β brace selects the middle letters, `ON`.
- Lower right: an `M` shown asking a question = `M ASK` = `MASK`. The γ marker selects its third letter, `S`.
- Concatenating `α γ β` gives `PRI` + `S` + `ON` = `PRISON`.

## Candidate ranking

1. `PRISON` — fully determined by all three rebuses and marked extraction.
2. No competing parse preserves `SPRING`, `SONG`, `MASK` and the extraction order.

## Submissions

- `PRISON` — correct (HTTP 200, 2026-07-12T11:07:11.924Z).

## Resolution

- Final answer: `PRISON`
- Incorrect count: 0
- Outcome: `correct`

## Stopping criteria

- Require a reproducible rebus reading/extraction before submission.
- End as `correct`, evidentially exhausted `cannot_do`, or `wrong_20` after exactly 20 incorrect submissions.
