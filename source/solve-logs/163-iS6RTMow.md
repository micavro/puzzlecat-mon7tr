# Solve log — 成语与反义词 (`iS6RTMow`)

Owner: `codex-sub-x-20260713`

## Observations

- Archived locally; one image resource.
- The image depicts a four-character idiom as structural blocks. Character 1 is left-right with its right side itself semi-enclosing; character 2 is left-right. Characters 3 and 4 are antonyms. The two red left components are requested as answers 1 and 2.
- Flavor emphasizes that any method is allowed.

## Reasoning

I downloaded public linguistic reference data only (CJKVI IDS character decompositions, a public idiom lexicon, and a public antonym lexicon), then intersected and visually checked the constraints.

- character 1: top-level `⿰`, with its right child an enclosure-type IDS;
- character 2: top-level `⿰`;
- characters 3 and 4: an attested antonym pair;
- all four characters form an attested idiom.

The initial over-strict search forced the blue/yellow portion to be a formal IDS enclosure and produced `继绝存亡`; all answer formats derived from that were rejected. The image explicitly warns that blue/yellow may *not* be a true semi-enclosure and that the two yellow portions are only “almost” alike. Relaxing that mistaken constraint gives the intended common idiom `拨乱反正`:

- `拨 = 扌 + 发`; the stylized blue/yellow right side is `发`.
- `乱 = 舌 + 乚`, matching the red-left plus green layout.
- The yellow `反` is visually close to the corresponding portion of `发`, explaining “几乎一样”.
- `反` / `正` are antonyms.

Thus red components 1 and 2 are `扌` and `舌`. The bottom answer diagram places the two red halves side by side inside one square rather than as two separate output cells: `扌 + 舌 = 括`. This also explains the conspicuous parenthetical remarks (括号) in the image. Final answer: `括`.

## Candidate ranking

1. `括` — strongest and complete: combines the two extracted red components into the single square shown at the bottom.
2. `扌舌`, `手舌` — rejected because the two parts must be composed, not concatenated.
3. `继绝`, `纟纟`, `绞丝旁`, `丝丝` — rejected wrong-idiom branch.

## Submissions

- `纟纟` — incorrect (`X`). The mechanism remains unique; the verdict indicates answer-format mismatch.
- `绞丝旁` — incorrect (`X`). This rejects the radical-name format.
- `丝丝` — incorrect (`X`). This rejects the two-character textual radical format.
- `继绝` — incorrect (`X`). This rejects the entire `继绝存亡` branch, not merely radical formatting.
- `扌舌` — incorrect (`X`). The idiom mechanism remains strong; next test the canonical character form `手舌` rather than the radical variant.
- `手舌` — incorrect (`X`). This proves that the two extracted parts must be recombined according to the bottom square diagram.
- `括` — correct (`回答正确！`).

Incorrect count: 6.

## Stopping criteria

Require a unique candidate supported by the idiom/antonym mechanism. Stop on correct, 20 incorrect, or `cannot_do` if evidence cannot distinguish candidates.
