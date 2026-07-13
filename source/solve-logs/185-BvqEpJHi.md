# Solve log: 文字游戏 (`BvqEpJHi`)

Owner: `recover-w3-20260712`

## Observations

- Examples: `2-7=b`, `4-7=dl`, `6-7=z`, `8-7=th`, `21-16=h`, `23-16=s`; target `1=?`.
- Right sides are lowercase letter sets/strings of varying length, so the hyphen likely separates two numeric properties or reference positions rather than ordinary subtraction.
- Answer checking is case-sensitive and does not strip punctuation, making exact output format significant.
- A free hint titled `完全看不懂……` exists, but its body is not present in the archive because it was not purchased at capture time. Root has been asked to reveal this zero-cost hint through the authorized browser.
- The revealed free hint says `其实这种文字游戏的数字上限是24`, independently confirming the 24-letter Greek alphabet.

## Tested rule families

- Ordinary differences, modular arithmetic, XOR, base conversion, primes/Fibonacci: do not fit the outputs.
- A1Z26/Caesar shifts and alphabet intervals: do not reproduce the multi-letter results.
- English/Chinese number-name subtraction or shared letters: inconsistent across examples.
- Seven-segment display subtraction/overlay: `6-7` and `8-7` would not yield the distinct listed outputs.
- Periodic-table atomic-number differences: only the first example coincidentally resembles boron (`7-2=5 -> B`).
- Keyboard, phone keypad, Roman numeral, Morse, and Braille interpretations tested so far do not fit all six examples.

## Solved rule

- Numbers index the Greek alphabet, and subtraction removes the letters of the second Greek-letter name from the first.
- `2-7`: `beta - eta = b`.
- `4-7`: `delta - eta = dl`.
- `6-7`: `zeta - eta = z`.
- `8-7`: `theta - eta = th`.
- `21-16`: `phi - pi = h`.
- `23-16`: `psi - pi = s`.
- Therefore Greek letter 1 is `alpha`.

## Candidate ranking

1. `alpha` - uniquely determined by the rule and lowercase formatting of every example.

## Submissions

- Serialized submission of `alpha` returned `alreadySolved: true` with no new attempt. This is consistent with the independently proven answer and the shared account having become solved while the browser lock was contended.

Incorrect count: 0.

Stopping criterion reached: the rule and free hint uniquely establish lowercase `alpha`, and the work command confirms the shared account is already solved.
