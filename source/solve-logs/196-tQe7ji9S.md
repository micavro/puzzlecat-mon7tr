# Solve log: 明诚谜007

## Status

- Owner: `chat2-w3-20260712`
- Puzzle ID: `tQe7ji9S`
- State: correct
- Incorrect submissions: 0

## Observations

- The puzzle consists of one image and asks for the coordinates of three airplane noses.
- Coordinates must be concatenated in ascending row-letter order, e.g. `A3B2C1`.
- The page says there are three intermediate-answer checks.
- Site cooldown after a wrong answer: 3 minutes.
- The grid is 10 rows (`A`-`J`) by 12 columns (`1`-`12`).
- Given blue body cells: `D4 D5 D6 D7 D8 E3 E6 F2 F4 F6 F8 F9 G3`.
- Forbidden dark-gray cells: `A9 B3 B9 C3 C9 D1 D3 D9 E4 E5 F12 G2 G4 G7 G8 H6 I6 J6 J9`.
- All three pictured shapes are drawn with their nose above the body. Relative to a nose at `(0,0)`, their body cells are:
  - Shape 1: `(-2,1) (-1,1) (0,1) (1,1) (2,1) (0,2) (-1,3) (0,3) (1,3)`.
  - Shape 2: `(-1,1) (0,1) (1,1) (-2,2) (0,2) (2,2) (0,3) (-1,4) (0,4) (1,4)`.
  - Shape 3: `(0,1) (-2,2) (-1,2) (0,2) (1,2) (2,2) (0,3) (-1,4) (1,4)`.

## Reasoning

- Enumerated every translation and each of four 90-degree rotations for each shape.
- Rejected placements that leave the grid, touch a forbidden cell, or put a nose on a given blue body cell.
- Combined exactly one placement of each shape, requiring no overlap and requiring the union to cover all 14 given blue cells.
- Legal single-shape placement counts after boundary/wall filtering were 18, 10, and 14.
- Exactly one three-shape combination satisfies all constraints:
  - Shape 1: nose `A6`, orientation as pictured (downward).
  - Shape 2: nose `F10`, rotated 90 degrees.
  - Shape 3: nose `H3`, rotated 180 degrees.
- Sorting the nose coordinates by row letter yields `A6F10H3`.

## Candidate ranking

- 1. `A6F10H3` — uniquely forced by exhaustive placement enumeration.

## Submissions

- `A6F10H3` — correct (`恭喜你，回答正确！`).

## Result

- Final answer: `A6F10H3`
- Incorrect submissions: 0
- The answer was uniquely determined before submission; no intermediate checks were needed.

## Stopping criteria

- Submit only a candidate uniquely forced by the image constraints.
- Stop at correct, at 20 incorrect submissions, or earlier as `cannot_do` if the archived evidence cannot distinguish candidates.
