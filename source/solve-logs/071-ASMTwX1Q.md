# Solve log — ASMTwX1Q

- Owner: `codex-sub-i-20260712`
- Title: 【星谜001】漏墨
- Status: correct
- Incorrect submissions: 0

## Observations

- Ink-obscured multiple-choice algebra problem; instruction says submit the option letter, not its numeric content.
- Visible structure reconstructs as `若 |m-n-3| + (m+n+1)^2 = 0，则 m+2n 的值为（ ）`; option B visibly corresponds to `-3`.

## Reasoning and candidate ranking

- Both `|m-n-3|` and `(m+n+1)^2` are nonnegative, so their sum is zero only if each is zero:
  - `m-n-3=0`
  - `m+n+1=0`
- Adding gives `2m-2=0`, hence `m=1`; then `n=-2`.
- Therefore `m+2n = 1-4 = -3`, which is option `B`.

Candidate ranking:

1. `B` — exact reconstruction and algebraic solution.
2. No runner-up.

## Submissions and verdicts

- `B` — correct (`你真棒！送你一朵小红fa^ω^`), HTTP 200. Incorrect count: 0.

## Stopping criteria

- Resolve `correct` on an accepted structurally derived answer.
- Resolve `cannot_do` when evidence cannot distinguish a justified candidate.
- Resolve `wrong_20` after exactly 20 incorrect submissions.
