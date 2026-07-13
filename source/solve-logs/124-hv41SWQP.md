# Solve log

- Owner: `recover-w3-20260712`
- Puzzle: `hv41SWQP`
- Title: 启动
- Incorrect submissions: 2 / 20
- Status: correct

## Observations

- The puzzle consists only of one image.
- The green and red power icons denote 开 and 关 respectively.
- The shared gate/door icon denotes 门. The two examples therefore read 开门见山 and 关门打狗: an eye/seeing icon plus mountains gives 见山, while a fist/striking icon plus dog gives 打狗.
- The bottom row has a single person/running-man pictogram, a yellow slot numbered 1, and the red 关 icon; after the comma it has the same person multiplied by 10000, a yellow slot numbered 2, and the green 开 icon.

## Reasoning

- The unique familiar expression matching those fixed pieces is `一夫当关，万夫莫开`.
- Thus the person icon supplies 夫 (single occurrence preceded by the understood 一), the multiplied person supplies 万夫, and the two numbered yellow slots are `当` and `莫` in order.
- The checker rejected both direct concatenation `当莫` and the full expression. The crucial remaining visual distinction is that slot 1 is a single yellow square, while slot 2 is only the middle yellow band of a three-part vertical box.
- Decompose the second missing character `莫` vertically as `艹 / 日 / 大`. Its highlighted middle band is therefore `日`. Slot 1 takes the whole missing character `当`; numbered extraction gives `当日`, a normal Chinese word. This accounts for every part of the otherwise unexplained slot geometry.

## Candidate ranking

1. `当日` — slot 1 is 当; highlighted middle component of slot-2 character 莫 is 日.
2. `一夫当关万夫莫开` — completed expression; rejected by the checker.
3. `当莫` — direct numbered-slot extraction; rejected by the checker.

## Submissions

- `当莫` — incorrect (2026-07-12 23:59 CST). This falsifies direct concatenation of the two missing characters.
- `一夫当关万夫莫开` — incorrect (2026-07-13 00:01 CST). The completed proverb is only an intermediate.
- `当日` — correct (2026-07-13 00:03 CST).

## Stopping criteria

- Reached a correct verdict after 2 incorrect submissions. Final answer: `当日`.
