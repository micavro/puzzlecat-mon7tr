# Solve Log: KowXEjGS

- Title: `编程`
- Draw: `tmp/practice-draw.json` (`2026-07-12T03:23:23.740Z`)
- Solver: child agent coordinated by root
- Submission limit: 20 incorrect answers
- Started: `2026-07-12` (Asia/Shanghai)

## Observations

- Puzzle archived locally with no external resources.
- The body is a short C++ program intended to read an integer and print whether it is prime.
- Several obvious source-code letters are replaced by question marks or numbered parenthetical blanks.

## Reasoning

1. Restore the four numbered blanks from standard C++ syntax/output:

   | Fragment | Restoration | Numbered letter |
   | --- | --- | --- |
   | `#inclu(3)e<bits/stdc++.h>` | `#include<bits/stdc++.h>` | `(3) = D` |
   | `(1)in>>a;` | `cin>>a;` | `(1) = C` |
   | `??ut<<"y(4)s";` | `cout<<"yes";` | `(4) = E` |
   | `?(2)ut<<"y?s";` | `cout<<"yes";` | `(2) = O` |

2. Reading the numbered replacements in order `(1)(2)(3)(4)` gives `C O D E`.
3. The unnumbered `?` characters merely complete the repeated words `cout` and `yes`; they are not part of the ordered extraction.
4. The loop condition in the archived text is `i%a==0`, whereas a functioning primality check would normally use `a%i==0`. This apparent coding error does not affect the letter-fill extraction and supplies no competing numbered letter.

## Candidate

- `CODE` — confidence `0.99`.

## Attempts

1. `CODE` - correct.

Evidence: `submissions/2026-07-12T03-25-30-083Z/submission.json`. Final incorrect count: `0 / 20`.
