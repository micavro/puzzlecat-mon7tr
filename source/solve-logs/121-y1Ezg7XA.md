# Solve Log: y1Ezg7XA

- Title: `古老迷宫游戏`
- Owner: `recover-root-20260712`
- Status: correct
- Incorrect submissions: 0

## Observations

- The single image contains six rows of large geometric symbols and six corresponding 3x3 dot grids.
- Each dot grid supplies a runner position and initial direction; the first also shows an example U-shaped route ending at a star.
- The six symbol-row lengths are approximately 6, 8, 5, 8, 5, and 6.
- Symbols are built from a central square or an open hourglass plus four diagonal arms. Arms may be connected to the center or detached.
- Strong working model: each symbol represents a local maze state or relative turn. Simulating each row from its supplied start state should trace one output glyph on the 3x3 dots, likely yielding a six-character answer.

## Mechanism

- The large symbols are first-person perspective views from an early maze game.
- For every view, advance one grid edge in the current heading, then apply the view at the newly reached point:
  - uninterrupted corridor: keep heading;
  - gap on the left/right before a front wall: turn left/right;
  - boxed dead end: reverse or terminate as shown;
  - explicit arrows disambiguate junction choices.
- The first row validates the convention: starting downward, the six views give `D,D,R,R,U,U`, exactly the supplied U-shaped route to the star.
- Applying the same rule to all six rows traces block letters `U N F O L D`. The third row uses explicit right-turn and U-turn marks and retraces the middle arm to form `F`.

## Candidate

- `UNFOLD`
- Confidence: 0.95

## Result

- Submitted `UNFOLD`.
- Verdict: correct.
- Incorrect submissions: 0.

## Guardrails

- Do not submit game-title guesses until one rule explains all six rows and extracted glyphs.
- Use only `npm run work -- submit recover-root-20260712 y1Ezg7XA "<ANSWER>"` for submissions.
