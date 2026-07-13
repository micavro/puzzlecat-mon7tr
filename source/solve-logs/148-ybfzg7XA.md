# ybfzg7XA - 小学生必背

Owner: `codex-root-20260712`

## Puzzle

The image gives three Chinese-character equations:

- 天 - 火 = 2
- 医 - 匪 = 10
- 消费 - 铁路 = ?

The title is “小学生必背”. The puzzle is an old Feigu Matrix item, originally dated 2017-07-16.

## Work

- Ordinary simplified-character stroke-count subtraction does not fit the examples: 天/火 are 4/4 strokes and 医/匪 are 7/10 strokes.
- Pinyin letter counts, alphabet sums, T9 sums/products, tones, radicals, and common-stroke multisets do not produce both 2 and 10.
- The typography suggests possible graphical subtraction/overlap. I extracted the original glyph masks and compared overlays. 天 can be thought of as leaving 二 after cancelling the lower person-like part against 火, but the same informal rule does not uniquely explain 医/匪 or determine the final expression.
- A low-confidence arithmetic candidate is `4`: 消(10)+费(9)=19 and 铁(10)+路(13)=23, whose absolute difference is 4. This does not explain the displayed examples and therefore is only a probe, not a solved mechanism.
- The closed mechanism is public-service telephone numbers, a set of numbers commonly memorized by schoolchildren:
  - 天 = weather forecast `121`; 火 = fire alarm `119`; `121 - 119 = 2`.
  - 医 = medical emergency `120`; 匪 = police alarm `110`; `120 - 110 = 10`.
  - 消费 = consumer complaint hotline `12315`; 铁路 = railway customer service `12306`; `12315 - 12306 = 9`.

## Submissions

- `4` - incorrect (low-confidence stroke-count probe; attempt 1).
- `9` - correct, derived from the complete hotline-number mechanism.

## Stop rule

Only candidates supported by a coherent rule or a strongly informative probe will be submitted. If the two examples remain underdetermined after those probes, resolve `cannot_do` rather than enumerate numbers.
