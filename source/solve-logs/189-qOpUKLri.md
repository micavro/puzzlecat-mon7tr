# Solve log: 无需多言 (`qOpUKLri`)

Owner: `recover-w1-20260712`

## Initial false lead

I initially treated the bottom `8-5-1-1` as a Chinese four-corner lookup. That produced `鈍/钝` (with obscure alternate `鉎`) but was falsified by the site.

## Correct mechanism

Connect each left outline/symbol to the matching right pictogram to form standard signs:

- `P` + car = blue `PARKING LOT` sign.
- Triangle + radiation = yellow `WARNING` sign.
- Diamond/placard + flame = red `FIRE` sign.
- Door + running person = green `EXIT` sign.

The bottom colors order these four concepts and the digits give 1-based extraction indices:

- Blue: `PARKINGLOT[8] = L`
- Yellow: `WARNING[5] = I`
- Red: `FIRE[1] = F`
- Green: `EXIT[1] = E`

This spells `LIFE`. The title fits because pictorial safety/traffic signs communicate without words, and following them protects life.

## Candidate ranking

1. `LIFE` - exact four-color indexed extraction and thematic confirmation.
2. `钝` / `鈍` - rejected false lead.

## Submissions

- `钝` - incorrect (attempt 1).
- `钝` - duplicate request, HTTP 400 and not counted as an attempt.
- `鈍` - incorrect (attempt 2).
- `钝` - incorrect (attempt 3).
- `LIFE` - correct (attempt 4).

Incorrect count: 3.

Stopping criterion met: accepted.
