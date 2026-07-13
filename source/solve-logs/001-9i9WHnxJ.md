# Solve log — 9i9WHnxJ《#1》

- Owner: `codex-sub-z-20260713`
- Status: correct
- Incorrect submissions: 1
- Answer: `CORRECT`

## Observations and reasoning

- The image contains seven separated groups: `F`, `E`, `I`, `I`, two vertically stacked `F`s, `F`, and overlapping `G`+`I`.
- The flavor explicitly says the place looks like a `猪圈`, pointing to the Pigpen cipher. All source letters lie in the first Pigpen 3×3 alphabet block (`A`–`I`), and the erratum says none were rotated/flipped, so preserve their printed placement while replacing each with its Pigpen stroke shape.
- The resulting block-letter silhouettes read `C O L L E C T`: a single `F` gives the three-sided C, `E` gives the closed O, each `I` gives an L corner, the two stacked `F` symbols combine into E, another `F` gives C, and the overlapping `G`/`I` corners combine into T.
- Candidate: `COLLECT`.
- `COLLECT` triggered the puzzle's explicit intermediate-answer milestone, confirming the Pigpen silhouette read and providing the next instruction.
- First follow-up hypothesis (“collect all glyphs” → central-box `E`) was rejected.
- The milestone is better read as a correction of the near-miss, not as the instruction `COLLECT`: it explicitly warns that no source letter is rotated/flipped. Keeping the canonical Pigpen orientations changes the two middle corner reads from the visually tempting `L L` to the corresponding right-oriented `R R`; the seven silhouettes then read `C O R R E C T`. This also matches the red flavor label `勘误` (“correction”) and the milestone's role of correcting `COLLECT`.

## Submissions

- `COLLECT` — intermediate; message: “本题中，所有字母都未经过旋转/翻转。”
- `E` — incorrect (misread `COLLECT` as an instruction; worker incorrect count 1).
- `CORRECT` — correct.

## Stopping criterion

- Use only mechanism-supported submissions; maximum 50 wrong answers.
