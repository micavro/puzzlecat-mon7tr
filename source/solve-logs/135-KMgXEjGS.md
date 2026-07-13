# Solve log: KMgXEjGS - 大厂笔试题

## Coordination

- Owner: `recover-w1-20260712`
- Current puzzle ID is case-sensitive `KMgXEjGS`.
- The Windows archive path collided with the previously solved `KmGXEjGS`; that puzzle's log is preserved as `solve-log-KmGXEjGS.md`, and its solver/submission artifacts were not used for this puzzle.
- Answer policy: no cooldown.
- Submission limit: stop at 20 incorrect answers.

## Observations

- The image has seven left-side characters: `会 提 现 二 直 学 儿`.
- Seven shuffled bottom characters are: `径 前 十 女 议 实 科`.
- Pairing them into ordinary two-character Chinese words gives:
  - `会议`
  - `提前`
  - `现实`
  - `二十`
  - `直径`
  - `学科`
  - `儿女`
- To the right are seven English answer lines of lengths 10, 7, 7, 6, 8, 7, and 8, respectively, with one red extraction position per line.

## Translation and extraction

| Chinese | English | Length | Red position | Letter |
|---|---|---:|---:|---|
| 会议 | `CONFERENCE` | 10 | 3 | N |
| 提前 | `ADVANCE` | 7 | 7 | E |
| 现实 | `REALITY` | 7 | 6 | T |
| 二十 | `TWENTY` | 6 | 3 | E |
| 直径 | `DIAMETER` | 8 | 3 | A |
| 学科 | `SUBJECT` | 7 | 1 | S |
| 儿女 | `CHILDREN` | 8 | 7 | E |

- The extracted string is `NETEASE`.
- NetEase is the English name of `网易`, matching the title's “大厂”.

## Candidate ranking

1. `网易` - exact company identified by the extraction `NETEASE`.
2. `NETEASE` - same answer in extracted English form; only needed if the site rejects the Chinese company name.

## Submissions

| # | Answer | Verdict |
|---|---|---|
| 1 | `网易` | Incorrect (`不对哦，再想想~`) |
| 2 | `NETEASE` | Correct (`恭喜你，回答正确~`) |

Incorrect count: **1**

## Revision after submission 1

- The Chinese company name was rejected despite the exact extraction. The puzzle has both English and Chinese tags, and the image directly spells `NETEASE`; submit that exact extracted form next.

## Final result

- Accepted answer: `NETEASE`.
- Incorrect submissions: **1**.
- The extraction is exact; no further submissions required.

## Stopping criteria

- Resolve `correct` immediately when `网易` or, if necessary, the exact extracted form `NETEASE` is accepted.
- Stop after 20 incorrect answers; stop earlier as `cannot_do` only if evidence becomes insufficient to distinguish candidates.
