# Solve Log: iD5RTMow

## Puzzle

- Title: `跳马2`
- Owner: `route-a-20260712`
- Status: solved locally; not submitted
- Incorrect count: 0

## Observations

- The board is 9 by 9.
- Every square must either contain a knight or be attacked by one knight move.
- No two knights may attack each other.
- Green fixed knights are at `r1c5`, `r3c2`, and `r3c8`; 11 more knights must be placed, for 14 total.
- Black cells cannot contain knights.
- The English crossword rows and selected columns provide letters for extraction. The prefilled first column reads `SQUIRREL`, confirming vertical clue 1.

## Knight placement

An exhaustive independent-dominating-set search gives exactly one placement of 14 knights under the stated constraints.

Fixed green knights:

- `r1c5`, `r3c2`, `r3c8`

Additional 11 knights:

- `r3c3`, `r3c7`
- `r4c3`, `r4c7`
- `r6c3`, `r6c7`
- `r7c2`, `r7c3`, `r7c7`, `r7c8`
- `r9c5`

Combined row-major coordinates:

`r1c5; r3c2,c3,c7,c8; r4c3,c7; r6c3,c7; r7c2,c3,c7,c8; r9c5`

## Crossword fill

Across answers needed for the extraction are:

1. `SID CAESAR` - an American comedian (`SIDCAESAR`)
2. `QUINTUPLE` - fivefold
3. `UNSELFISH` - a noble quality
4. `INCIVIL` - uncivilized
5. `RELIGIOSO` - religious, Italian
6. `ROADWAY` - road
7. `EPISCOPE` - reflecting projector
8. `LIMEWATER` - limewater
9. `SMILE` - smile

Cross-checks include:

- Column 1, rows 1-8: `SQUIRREL` = 松鼠.
- Column 3, rows 1-8: `DISCLAIM` = 放弃.
- The remaining supplied vertical clue is `REHIRE` = 重新雇用 and is consistent with the intended obscured/selected column letters.

## Extraction

Read the letters in all 14 knight cells in row-major order:

- `r1c5`: `A` from `SIDCAESAR`
- `r3c2,c3,c7,c8`: `NSIS` from `UNSELFISH`
- `r4c3,c7`: `CL` from `INCIVIL`
- `r6c3,c7`: `AY` from `ROADWAY`
- `r7c2,c3,c7,c8`: `PIPE` from `EPISCOPE`
- `r9c5`: `S` from `SMILE`

This spells:

`ANSISCLAYPIPES` -> `ANS IS CLAY PIPES`

Therefore the final answer is `CLAY PIPES`.

## Candidate ranking

1. `CLAY PIPES` - confidence 0.995. The knight layout is unique, the crossword entries are cross-checked, and the extracted text explicitly states the answer.

## Submission history

- No submissions.
- Incorrect count: 0.

## Recommendation

Submit `CLAY PIPES`.
