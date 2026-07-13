# Solve Log: WTklljce - 成词成对

- Owner: `chat2-w3-20260712`
- Status: correct
- Incorrect submissions: 0
- Stop rule: submit only candidates supported by the pairing/extraction mechanism; stop at 20 incorrect or earlier if evidence cannot distinguish candidates.

## Observations

- Archive completed with no external resources; all puzzle data is HTML/text.
- Six five-letter word pairs are shown; the first two are `FUNNY — LATTE` and `KNEED — FIZZY`.
- Every pair is related by applying one uniform Caesar shift to all five letters.

## Reasoning

- `FUNNY +6 = LATTE`.
- `KNEED +21` (equivalently -5) `= FIZZY`.
- Completing the same mechanism gives `APTLY +19 = TIMER`, `RIVER +9 = ARENA`, `DAZED +15 = SPOTS`, and `EMOTE +14 = SACHS`.
- Reading the six positive shift values as A1Z26 gives `6,21,19,9,15,14` -> `FUSION`, matching the stated enumeration `(6)`.
- The checker identifies `FUSION` as an intermediate. Applying the displayed `(6)` as one more Caesar shift gives `FUSION +6 = LAYOUT` exactly, so `LAYOUT` is the final paired word.

## Candidate ranking

- 1. `LAYOUT` - exact continuation of the same mechanism: `FUSION +6`.
- Intermediate: `FUSION` - exact extraction from all six row shifts; checker-confirmed as intermediate.

## Submissions

- `FUSION` - intermediate (`中间提示`), not incorrect.
- `LAYOUT` - correct (`恭喜你，回答正确！`).
