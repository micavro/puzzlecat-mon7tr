# Solve log — 福尔摩斯

- Puzzle ID: `Zeipgd2S`
- Owner: `codex-sub-m-20260712`
- Status: correct
- Incorrect submissions: 1

## Observations and reasoning

- Archived locally; independent solve only.
- The prose is camouflage around Morse punctuation. My first pass missed the interpunct between `夏洛克•福尔摩斯`: line 1 has three interpuncts plus the final period, `....` = H (not S). Line 2 has three dash/underscore separators, `---` = O. Line 3 has two dot-like punctuation marks followed by a dash, `..-` = U. Line 4 ends in `...` = S. Line 5's literal `点` supplies `.` = E.
- Thus the five lines spell `HOUSE`, with lines 3 (`怎么看—用眼睛看`) and 5 (`雨点`) also hinting to look at dots visually.

## Candidate ranking

- 1. `HOUSE` — complete five-line Morse extraction `.... / --- / ..- / ... / .`.
- 2. `SOS` — rejected first-pass result caused by overlooking the third interpunct in line 1 and ignoring lines 3/5 as data.

## Submissions

- `SOS` — incorrect (attempt 1).
- `HOUSE` — correct (attempt 2).

## Final classification

- `correct`, answer `HOUSE`, incorrect count 1.

## Stopping criteria

- Resolve on confirmed verdict; stop if evidence cannot distinguish a candidate; maximum 20 incorrect.
