# yC1zg7XA - 相生相克

- Owner: `chat2-w2-20260712`
- Status: solving
- Incorrect submissions: 0
- Stopping rule: submit only mechanism-supported values; stop at correct, evidence exhaustion, or 20 incorrect.

## Identification

The five clues identify `黑塔` / `HERTA` from *Honkai: Star Rail*:

- The requested intermediate has five letters: `HERTA`.
- Herta is an ice-damage character.
- Her Chinese name is `黑塔`: `黑` contains `灬`, and `塔` contains `土`.
- Her puppet/body lore explains the return-to-youth clue, while her collection of curios explains the rare-object clue.

Because the five statements are printed in the order `金、木、水、火、土`, they assign letters as follows:

| Element | Letter |
| --- | --- |
| 金 | H |
| 木 | E |
| 水 | R |
| 火 | T |
| 土 | A |

## Extraction

- Start at metal and follow the forward overcoming cycle: `金克木、木克土、土克水、水克火、火克金`.
  - Order: `金木土水火`
  - Letters: `H E A R T`
  - Result: `HEART`
- Start at metal and follow the generating cycle in reverse. The forward generating cycle is `金生水、水生木、木生火、火生土、土生金`, so its reverse from metal is `金土火木水`.
  - Letters: `H A T E R`
  - Result: `HATER`

## Candidate ranking

1. `HERTA` - explicitly marked intermediate answer; submit first to obtain any checker milestone.
2. `HEART` / `HATER` - the two exact five-letter extractions requested by the final two blanks. Checker behavior will determine whether either alone or their combination is final.

## Submissions

- `HERTA` - intermediate, checker message `金木水火土=HERTA`; incorrect count remains 0.
- `HEART` - intermediate, checker message `木█水█金█金█土█木█`; mapped through `金木水火土=HERTA`, the visible element sequence gives `E R H H A E` and appears to be one half of a further interleaving.
- `HATER` - intermediate, checker message `█土█火█火█木█火█水`; incorrect count remains 0.

Overlaying the two checker strings at their black squares gives:

`木土水火金火金木土火木水`

Applying `金木水火土 = H E R T A` gives:

`E A R T H  T H E A T E R` = `EARTH THEATER`.

Final candidate: `EARTH THEATER`.
- `EARTH THEATER` - correct.

## Resolution

- Outcome: `correct`
- Final answer: `EARTH THEATER`
- Incorrect submissions: 0 (all three earlier submissions were accepted intermediates).
