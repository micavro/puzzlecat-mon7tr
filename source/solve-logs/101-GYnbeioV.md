# Solve Log: GYnbeioV

- Title: `克制关系`
- Owner: `recover-root-20260712`
- Status: correct
- Incorrect submissions: 7
- Answer: `DROWN`

## Observations

- Example: water overcomes fire.
- Each unknown has `(index/length)` for extracting one letter from the English answer.
- Gold/metal overcomes wood: `WOOD` (4/4) -> `D`.
- `WOOD` was accepted as an intermediate answer, confirming row 1 and extracting `D`.
- The remaining relations are not yet established; the earlier `DRAWN` hypothesis was rejected.

## Submissions

- `WOOD` - intermediate (not counted as incorrect)
- `DRAWN` - incorrect
- `MAGNET` - incorrect
- `CUTTER` - incorrect
- `SHEARS` - incorrect
- `DRIFT` - incorrect
- `DRIFT` - incorrect (accidental duplicate: the first lock-waiting command completed after initially returning no record)
- `HIGHER` - incorrect
- `DROWN` - correct

## Verification Plan

- Current constrained extraction candidate is `DRIFT`:
  - `WOOD` -> D (confirmed intermediate)
  - `HIGHER` card -> I
  - `FENCE` blocks wind -> F
  - `TNT` destroys a car -> T
  - Row 2 must supply R; its exact Qiaohu relation remains unidentified.
- `DRIFT` was rejected. The two identical records document a lock-race mistake; do not retry commands solely because their first output is empty without a delayed record check.
- Use intermediate validation only for independently justified row words before attempting another final extraction.

## Final mechanism

- `WOOD` gives `D` and was confirmed as an intermediate.
- The playing-card counter is `JOKERS` (2/6), giving `O`, rather than `HIGHER`.
- `WALLS` (1/5) block wind, giving `W`.
- `GUN` (3/3) can destroy/stop a car, giving `N`.
- The character row supplies `R`, so the extraction is `DROWN`; the opening water-versus-fire example reinforces the result.
