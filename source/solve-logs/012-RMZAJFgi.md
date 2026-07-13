# Solve log: RMZAJFgi

- Owner: `recover-w1-20260712`
- Status: correct
- Incorrect submissions: 0
- Answer policy: fixed 1-minute cooldown; stop at 20 incorrect submissions.
- FPA check: no FPA tag. Tags recover as approximately `一枚`, `英文`, `猜规则`.

## Observations

- Title: `[旧题] bitop`.
- The flavor text says this was a group from a daily puzzle collection published in May 2025. In the original, each sub-puzzle was judged separately; here, submitting an answer believed correct for any sub-puzzle yields one character of the final answer.
- Seven images are present: two worked examples (`note`, `standby`) and five target items (`corn`, `notmore`, `abandon`, `horrors`, `landform`).

## Reasoning

- `bitop` means bitmap/bitwise operations on glyphs. The operation name is embedded between operand letters in the answer word.
- Worked example `NOTE` parses as `NOT E`: the image is a white lowercase `e` on a black background, i.e. bitmap inversion.
- Worked example `STANDBY` parses as `ST AND BY`: pairwise bitmap intersection of the two-letter strings produces the two displayed fragmentary glyphs.
- Target 1 parses as `C OR N` = `CORN`; the displayed glyph is the bitmap union of `c` and `n`.
- Target 2 parses as `NOT (M OR E)` = `NOTMORE`; its inverted black/white rendering matches NOT applied to a union.
- Target 3 parses as `AB AND ON` = `ABANDON`; the two output glyphs are pairwise intersections (`a` AND `o`, `b` AND `n`).
- Target 4 parses as `H OR R OR S` = `HORRORS`; the single glyph is the union of `h`, `r`, and `s`.
- Target 5 parses as `L AND F OR M` = `LANDFORM`; the single glyph results from the indicated left-to-right bit operations.
- The flavor explicitly says a sub-puzzle answer should be submitted to obtain one position of the final answer. Therefore these five words are validator keys, not necessarily the final answer.

## Candidate ranking

1. `CORN`, `NOTMORE`, `ABANDON`, `HORRORS`, `LANDFORM` — exact target sub-answers, to query validator feedback.
2. `QUBIT` — after the first three validator messages give `QUB__`, this is the strongly determined five-letter thematic final answer (a quantum bit), matching title and bit-operation theme. Submit next.

## Submissions

- `CORN` — **intermediate**, message: `答案的第一位为 Q。` Final answer position 1 = `Q`; incorrect count remains 0.
- `NOTMORE` — **intermediate**, message: `答案的第二位为 U。` Final answer position 2 = `U`; incorrect count remains 0.
- `ABANDON` — **intermediate**, message: `答案的第三位为 B。` Final answer position 3 = `B`; incorrect count remains 0.
- `QUBIT` — **correct**, site message: `恭喜你，回答正确！`; incorrect count 0.

## Final

- Answer: `QUBIT`
- Incorrect count: 0
- Stopping criterion: correct verdict received.
