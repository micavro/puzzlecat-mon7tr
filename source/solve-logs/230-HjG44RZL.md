# HjG44RZL - 留空

Owner: `chat2-root-20260712`

## Observations

- Archive completed with 12 files and one resource, with no failures.
- The image is not actually empty: it outlines the left side of a computer
  keyboard. The top wide key bears the standard Tab/back-tab arrow, and the
  wider keys below occupy the Caps Lock and Shift positions; adjacent letter
  keycaps are deliberately blank.
- The text explicitly says the answer is an animal. The flavor calls the puzzle
  an attempt at minimalism, and both available hint titles emphasize identifying
  what the mostly blank image represents and what kind of answer to give.

## Reasoning

- The minimal image represents a `keyboard`; the canonical animal phrase/meme
  completing that object is `Keyboard Cat`.
- Therefore the animal component to submit is `CAT`.
- `TABBY` is a tempting Tab-key wordplay, but the image establishes a whole
  keyboard via Tab/Caps/Shift geometry, not merely the letters TAB followed by
  two answer blanks. `Keyboard Cat` uses all visible evidence directly.

## Candidate ranking

- `CAT` - direct completion of the represented `Keyboard Cat`; strongest.
- `TABBY` - rejected as primary because the other modifier-key rows would be
  unexplained.

## Submissions

- `CAT` - incorrect (`2026-07-12T12:39:54.441Z`), rejecting the general
  `Keyboard Cat` completion.
- `TABBY` - incorrect (`2026-07-12T12:41:30.173Z`), rejecting simple
  concatenation from the Tab key.
- Total incorrect: `2 / 20`.
- Total incorrect: `1 / 20`.

## Reassessment

- Only the Tab key carries a symbol while all other keycaps are blank. `TAB`
  plus the animal completion `BY` gives `TABBY`; this is more local than the
  rejected whole-keyboard meme reading.
- Corrected mechanism: the modifier-key geometry identifies `TAB`, while its
  only visible mark is a left/backwards arrow. Reading the key name backwards
  gives `TAB -> BAT`, exactly an animal. This uses both the otherwise blank key
  labels and the arrow operation.

## Next controlled test

- `BAT` - uniquely derived by reversing `TAB`.

## Result

- `BAT` - correct (`2026-07-12T12:42:36.311Z`).
- Final status: `correct`; total incorrect: `2`.

## Stopping criteria

- Resolve `correct` after an accepted, mechanism-supported answer.
- Resolve `cannot_do` if evidence cannot distinguish candidates.
- Resolve `wrong_20` after exactly 20 incorrect submissions.
