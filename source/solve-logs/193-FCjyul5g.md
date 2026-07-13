# Solve Log: 明诚谜 005 (FCjyul5g)

- Owner: `route-a-20260712`
- Status: candidate ready; awaiting root submission
- Incorrect submissions: 0 / 20
- Last updated: 2026-07-13 (Asia/Shanghai)

## Observations

- The image has two rows of seven colored slots.
- Row clues are `北方菜` and `岳飞罪`.
- Positions 1, 3, 4, 6, and 7 are linked vertically as equal.
- The unlinked positions contain extraction labels: top row position 2 = 3, top position 5 = 4; bottom position 2 = 2, bottom position 5 = 1.
- The answer area requests a four-character answer in order 1, 2, 3, 4.

## Reasoning

1. Interpret the seven slots as unspaced pinyin letters.
2. A northern dish is `木须肉`, whose pinyin is `MUXUROU`:
   - positions: M U X U R O U
3. The alleged crime used against Yue Fei is `莫须有`, whose pinyin is `MOXUYOU`:
   - positions: M O X U Y O U
4. The two strings agree exactly at linked positions 1, 3, 4, 6, 7: M, X, U, O, U.
5. Extract the differing letters by their printed labels:
   - 1 = Y (bottom position 5)
   - 2 = O (bottom position 2)
   - 3 = U (top position 2)
   - 4 = R (top position 5)
6. Reading 1-2-3-4 yields `YOUR`.

## Candidates

1. `YOUR` - confidence 100%. Both clue fills, all equality markers, all numbered cells, and the requested answer length agree exactly.

## Submissions

- None.

## Stopping Criteria

- Submit `YOUR` once through the root worker's serialized submission command.
- Stop at 20 incorrect submissions, or earlier only if a verdict reveals an unexpected answer convention and no mechanism distinguishes alternatives.
