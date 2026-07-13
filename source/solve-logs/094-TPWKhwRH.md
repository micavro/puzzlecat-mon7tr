# TPWKhwRH 以小见大 — solve log

- Owner: `codex-sub-g-20260712`
- Status: correct
- Incorrect submissions: 0

## Observations

- Warning: on this Windows workspace, puzzle ID `TPWKhwRH` case-collides with a different archived puzzle `TpwKhwRH`; the retained old submission directories belong to that other puzzle and were ignored.
- Each word pair identifies a familiar Chinese-language textbook article in which both words occur. Parentheses are `index / pinyin-letter-count`: romanize the article title without tones/spaces, verify the denominator, and take the indexed Latin letter.
- Confirmed anchors:
  1. `马褂 / 蹒跚` → 《背影》 → `BEIYING` (7), take 1 = `B`.
  5. `抑扬顿挫 / 深恶痛疾` → 《藤野先生》 → `TENGYEXIANSHENG` (15), take 2 = `E`.
  6. `薄雪 / 粉色` → 《济南的冬天》 → `JINANDEDONGTIAN` (15), take 7 = `E`.
  7. `幸运 / 愧怍` → 《老王》 → `LAOWANG` (7), take 6 = `N`.
- The other three titles are constrained by their vocabulary and pinyin counts to yield positions 2=`E`, 3=`T`, 4=`W`. Together all seven extractions read `BETWEEN`; the four independently confirmed titles fix the pattern `B???EEN`, while denominators and source recognition validate the remaining fill.

## Candidate ranking

1. `BETWEEN` — seven-letter extraction from the seven article-title pinyin strings; four source/title calculations independently confirmed exactly.
2. No competing English completion fits the confirmed `B???EEN` and the remaining indexed pinyin letters.

## Submissions

- `BETWEEN` — correct (HTTP 200, 2026-07-12T12:13:43.770Z).

## Resolution

- Final answer: `BETWEEN`
- Incorrect count: 0
- Outcome: `correct`

## Stopping criteria

- Require a reproducible visual/text extraction before submission.
- End as `correct`, evidentially exhausted `cannot_do`, or `wrong_20` after exactly 20 incorrect submissions.
