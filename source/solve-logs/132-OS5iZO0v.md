# Solve log

- Owner: `recover-w3-20260712`
- Puzzle: `OS5iZO0v`
- Title: 回転
- Incorrect submissions: 0 / 20
- Status: correct

## Observations

- The image contains blank outlines of Japanese shogi pieces, kana appended beside them, a flip/rotation symbol, and rebus result pictures.
- The final instruction says the answer is a two-kanji food; katakana is also accepted.

## Reasoning

- A normal shogi piece read as `王` plus `む` gives `オウム`, matching the parrot picture.
- After the depicted turn/flip, `玉 + と` gives `玉兎` (`ぎょくと`, jade rabbit/moon), matching the rabbit-and-moon picture. This establishes that a piece's kanji/readings participate in the rebus.
- The third example is `角 + に = 角煮` (`かくに`), matching the pictured braised pork cubes. Therefore the relevant shogi piece is the bishop, `角`.
- When a bishop is turned over/promoted it becomes `馬` (from 龍馬), read `うま`. Substituting it into the red final pattern `し [piece] い` gives `し + うま + い = シウマイ`, the conventional spelling used for shumai.
- The requested two-kanji food spelling is `焼売`.

## Candidate ranking

1. `焼売` — exact two-kanji form of シウマイ.
2. `シウマイ` — explicitly allowed katakana form.

## Submissions

- `焼売` — correct (2026-07-13 01:18 CST).

## Stopping criteria

- Correct on the first submission. Final answer: `焼売`.
