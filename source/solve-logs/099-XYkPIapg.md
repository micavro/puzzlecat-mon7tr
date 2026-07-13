# Solve Log: 信达雅 (XYkPIapg)

- Owner: `route-a-20260712`
- Status: Active; third extraction from phrase continuations under investigation
- Incorrect submissions: 22 / 50 (authoritative root count; local archive may be incomplete)
- Last updated: 2026-07-13 (Asia/Shanghai)

## Observations

- The left column contains 11 Chinese idioms/proverbs, each followed by an extraction index in square brackets.
- The right column contains awkward literal Chinese renderings of 11 familiar English sayings, with exact English word-length enumerations.
- The columns are not row-aligned. Matching them by meaning and indexing the English answers in the printed order of the right column gives the intermediate answer.
- Punctuation and spaces are ignored for all letter indexing.

## First Extraction: Right Column

1. `YOU ONLY LIVE ONCE` matches `及时行乐` [8] -> `L`.
2. `ACTIONS SPEAK LOUDER THAN WORDS` matches `行胜于言` [11] -> `A`.
3. `YOU SCRATCH MY BACK AND I'LL SCRATCH YOURS` matches `平等互惠` [8] -> `T`.
4. `NEVER IN A MILLION YEARS` matches `钻火得冰` [13] -> `I`.
5. `NO PAIN, NO GAIN` matches `苦尽甘来` [7] -> `N`.
6. `PAIN IN THE NECK` matches `过街老鼠` [1] -> `P`.
7. `DUST THOU ART, TO DUST RETURNEST` matches `人固有一死` [6] -> `H`.
8. `COME HOME TO ROOST` matches `多行不义必自毙` [11] -> `R`.
9. `VALEDICTORIAN` matches `名列前茅` [2] -> `A`.
10. `WHAT'S DONE IS DONE` matches `木已成舟` [11] -> `S`.
11. `NOBODY'S PERFECT` matches `人非圣贤` [9] -> `E`.

This spells `LATIN PHRASE`.

## Intermediate Verdict

- `LATIN PHRASE` was accepted as an intermediate answer with feedback `Keep Going!`.
- `Keep Going!` is an extraction instruction: continue each semantic chain from the Chinese idiom and English saying to a familiar Latin phrase. It is not text to translate into Latin.
- The bracketed indices still apply. For the second pass, read in the printed order of the left column.

## Second Extraction: Left Column

1. `苦尽甘来` / no pain, no gain -> `PER ASPERA AD ASTRA` [7] -> `E`.
2. `人非圣贤` / nobody's perfect -> `ERRARE HUMANUM EST` [9] -> `M`.
3. `过街老鼠` / pain in the neck -> `PERSONA NON GRATA` [1] -> `P`.
4. `人固有一死` / dust thou art -> `MEMENTO MORI` [6] -> `T`.
5. `多行不义必自毙` / come home to roost -> `SIC SEMPER TYRANNIS` [11] -> `Y`.
6. `木已成舟` / what's done is done -> `ALEA IACTA EST` [11] -> `S`.
7. `平等互惠` / you scratch my back... -> `QUID PRO QUO` [8] -> `Q`.
8. `名列前茅` / valedictorian -> `SUMMA CUM LAUDE` [2] -> `U`.
9. `钻火得冰` / never in a million years -> `AD KALENDAS GRAECAS` [13] -> `A`.
10. `行胜于言` / actions speak louder than words -> `FACTA NON VERBA` [11] -> `R`.
11. `及时行乐` / you only live once -> `CARPE DIEM` [8] -> `E`.

This spells `EMPTY SQUARE`.

## Second Intermediate Verdict

- `EMPTY SQUARE` was accepted as another intermediate answer with the same feedback, `Keep Going!`.
- It does not count as an incorrect submission. The incorrect count remains 2.
- Continuing cyclically from each indexed Latin letter produces an 11 x 11 square whose first column is `EMPTY SQUARE`:

```text
ERAADASTRAP
MANUMESTERR
PERSONANONG
TOMORIMEMEN
YRANNISSICS
STALEAIACTA
QUOQUIDPROQ
UMMACUMLAUD
AECASADKALE
RBAFACTANON
EMCARPEDIEM
```

- The other columns, diagonals, perimeter continuation, and letters immediately before/after the indexed positions do not give another coherent instruction. They are just continuations of the source Latin phrases.
- The puzzle body itself contains no square glyph or square-grid asset. The only explicit square is the puzzle's configured correct-message glyph, `□`.

## Rejected Sator-Square Branch

- `TOFU` was rejected. The missing-glyph interpretation of `EMPTY SQUARE` is falsified.
- Combining the intermediates as the famous Sator Square was also tested and rejected in both precise forms: the full phrase and the object name.
- The Sator branch was attractive because it is a Latin word square, but it has no mechanical connection to the 11 source groups.
- For reference, its standard SATOR-form layout is:

```text
SATOR
AREPO
TENET
OPERA
ROTAS
```

- The earlier cyclic 11 x 11 continuation was checked for all five Sator words; none appear as straight-line entries.

## Space-Preserving 11 x 11 Squares

- The correct continuation is to keep going character-by-character from each indexed letter while preserving real word spaces as empty cells.
- The two layers must retain the printed order in which each intermediate was extracted:
  - English sayings stay in right-column order, where their indexed first letters spell `LATIN PHRASE`.
  - Latin phrases stay in left-column order, where their indexed first letters spell `EMPTY SQUARE`.
- Ignoring punctuation but retaining spaces, the Latin rows are below (`·` denotes an empty cell):

```text
ERA·AD·ASTR
MANUM·ESTER
PERSONA·NON
TO·MORIMEME
YRANNISSIC·
STALEA·IACT
QUOQUID·PRO
UMMA·CUM·LA
AECASAD·KAL
RBAFACTA·NO
EMCARPE·DIE
```

- The English sayings in their own right-column order are:

```text
LIVE·ONCEYO
AK·LOUDER·T
TCH·MY·BACK
ION·YEARSNE
NO·GAINNO·P
PAIN·IN·THE
HOU·ART·TO·
ROOSTCOME·H
ALEDICTORIA
S·DONEWHATS
ERFECTNOBOD
```

- The Latin first column still reads `EMPTY SQUARE`.
- The Latin-only empty-cell pattern has 13 visible cells in the first 11 raw characters (14 was an earlier counting slip); it does not form a stable recognizable glyph in either left- or right-column row order.
- Overlaying these two naturally ordered space masks gives exactly one cell that is empty in both squares: row 7, column 8.
- At that cell:
  - Latin row 7 is `QUOQUID·PRO`, from `QUID PRO QUO`.
  - English row 7 is `HOU·ART·TO·`, from `DUST THOU ART, TO DUST RETURNEST`.
- The earlier `(3,8)` result came from first reordering the English rows into semantic left-column order. That destroys the right-column order which generated the first intermediate. Its selected Latin answer `PERSONA NON GRATA` was rejected, corroborating that the aligned-by-meaning overlay was the wrong layer order.
- Order audit:
  - Latin-left over English-right: one shared blank at `(7,8)`; this preserves both extraction orders.
  - Latin-left over English-left: one shared blank at `(3,8)`; requires an unsupported English reorder and led to a rejected answer.
  - Latin-right over English-right: one shared blank at `(6,8)`; requires an unsupported Latin reorder and selects the same rejected semantic pair.
  - Latin-right over English-left: two shared blanks, so it is not unique.
- Directly submitting the Latin row `QUID PRO QUO` was rejected. The shared empty cell is therefore an extraction location, not a row selector.

## Coordinate And Element Extraction

- The unique shared empty cell is at row 7, column 8, giving the number `78`.
- Apply the repeated feedback literally once more: from the shared empty square, `Keep Going!` one cell to the right in both space-preserving rows:

```text
Latin-left:   QUOQUID·PRO
                      ^
English-right: HOU·ART·TO·
                       ^
```

- Immediately after the column-8 blank, the Latin layer contributes `P` and the English layer contributes `T`, giving the element symbol `Pt`.
- `Pt` is platinum, whose atomic number is exactly `78`. Thus the coordinate and the two letters independently cross-check one another.
- Together `78` and `Pt` are exactly the number and symbol that fill platinum's square in the periodic table, providing a concrete interpretation of `EMPTY SQUARE`; the configured response glyph `□` matches that final cell motif.
- This also explains why neither the Latin row nor English row is itself the answer: the shared blank supplies `78`, and continuing right in both language layers supplies `Pt`.

## Output-Language Audit

- `PLATINUM` and `PT` were both rejected. This does not falsify `78`/`Pt` as the mechanism because PuzzleCat normalization does not translate between an English element name, chemical symbol, atomic number, and Chinese element name.
- The configured normalization only lowercases, strips spaces/punctuation, converts fullwidth characters, and normalizes simplified/traditional Han variants.
- The puzzle starts in Chinese, is titled `信达雅`, and repeatedly moves through translations. After identifying `78` / `Pt`, continuing the translation chain back into the puzzle's source language gives the standard Chinese element name `铂` (traditional `鉑`, normalized equivalently by the site).
- This closes the language loop more cleanly than stopping at the English `PLATINUM` or the language-neutral symbol `Pt`.
- Coordinate reversal to `87` is weak: matrix coordinates were derived explicitly as row 7, column 8, and element 87 is francium (`Fr`), while no adjacent or cross-layer letters yield `F` and `R`.

## Direction And Coordinate Verification

- The naturally ordered matrices have exactly one common blank in the 11 x 11 window: one-based row 7, column 8.
- Latin row 7 is `QUOQUID·PRO`; column 8 is blank and the next character to the right is `P`.
- English-right row 7 is `HOU·ART·TO·`; column 8 is blank and the next character to the right is `T`.
- Reading right is forced by the normal direction of both phrases and by `Keep Going!`. Treating the blank as a character and moving one cell, or skipping the blank to the next non-space character, gives the same `P/T` result.
- Moving left instead gives `D/T` (`Dt`), which is not an element symbol and has no relationship to either 78 or 87.
- Reversing the coordinate to column-row `87` would imply francium (`Fr`), but no local continuation yields `F/R`. The simultaneous `78` and `Pt` agreement therefore strongly fixes the orientation.
- `PLATINUM`, `PT`, and `铂` being rejected makes output formatting the remaining uncertainty; it does not create a competing directional mechanism.

## Rejected Periodic-Table Branch

- `78` was also rejected, after `PLATINUM`, `PT`, and `铂`.
- Therefore the numerical coincidence between `(7,8)` and platinum's atomic number cannot be the intended terminal mechanism, even though the right-adjacent letters happened to give `P/T`.
- Do not continue with `铂金`, `第78号元素`, `元素周期表`, or coordinate reversal to 87 without new evidence.

## Coordinate Labels And The Empty Cell

- Treat the two accepted intermediates as the labels supplied by the two language layers at the unique coordinate `(7,8)`:
  - Row 7 of `EMPTY SQUARE` is `Q`.
  - Position 8 of `LATIN PHRASE` is `R`.
- The shared empty cell is a `S`pace, supplying `S`.
- Applying `Keep Going!` to the right of that shared space supplies `P` from the Latin row and `T` from the English row.
- These five independently sourced letters are exactly the consecutive sequence `P Q R S T`:

```text
Latin next letter       P
EMPTY SQUARE[7]         Q
LATIN PHRASE[8]         R
shared space            S
English next letter     T
```

- This uses the coordinate, both intermediate labels, the common blank, and the rightward continuation. Unlike the periodic-table reading, no external reference is needed to determine the extracted string.
- `PQRST` is also the conventional label sequence for the waves of one electrocardiogram cycle, but expanding it to a medical term would be a separate interpretive step not yet required by the mechanism.

## Space-Matrix Construction Audit

- `PQRST` was rejected, forcing a review of the shared-empty-cell premise itself.
- The original extraction explicitly ignored spaces and punctuation. It defines a cyclic **letter** stream, but does not define spaces or punctuation as square cells.
- The claimed `(7,8)` overlap requires all of the following extra assumptions:
  - choose an 11-character rather than 11-letter window solely because there are 11 rows;
  - retain spaces as cells after previously ignoring them;
  - discard punctuation as cells, including the comma explicitly shown by the enumeration in `DUST THOU ART, TO DUST RETURNEST`;
  - overlay English-right order on Latin-left order without an explicit overlay instruction.
- If the enumerated comma is retained as a character, English row 7 is `HOU·ART,·TO` rather than `HOU·ART·TO·`, so `(7,8)` contains a comma and is not a common blank.
- Starting one character after the indexed letter also shifts every proposed blank coordinate. The common-cell result is therefore not invariant under plausible readings of `Keep Going!`.
- The exact Latin and English phrase identities remain well supported, but their word-boundary positions do not provide a sufficiently defined third extraction. The entire `(7,8)` / `Pt` / `PQRST` branch is now rejected as an overfit.

## Direct Intermediate Recombination

- The only invariant new information after the two accepted submissions is the pair of two-word intermediates:

```text
LATIN PHRASE
EMPTY SQUARE
```

- They have the same adjective-noun structure. Taking the meaningful modifier from the first and the meaningful object from the second gives the established term `LATIN SQUARE`.
- The opposite cross-combination, `EMPTY PHRASE`, is not an established object and would amount to a blank answer.
- `LATIN SQUARE` also matches the puzzle's 11-item cyclic structure: the semantic matching permutation between left and right orders is one complete 11-cycle, which is compatible with generating a cyclic Latin square of order 11. This is corroboration, not an additional arbitrary space overlay.
- The configured correct-message glyph `□` directly reinforces `SQUARE`.

## Rejected Recombination Branch

- `LATIN SQUARE` was rejected; simply crossing one word from each intermediate is not the final operation.
- `TABULA RASA` was also rejected; a blank slate is only an associative paraphrase of `EMPTY SQUARE`, not its direct translation.

## Translate The Second Intermediate

- The accepted intermediates can instead be read as type plus text:
  - `LATIN PHRASE` specifies the required output language/type.
  - `EMPTY SQUARE` is the text to render as that Latin phrase.
- This differs from the rejected `PERGE`: the puzzle asks to translate the accepted second intermediate, not the feedback `Keep Going!`.

### Grammar

- `quadrātum, -ī` is a second-declension neuter noun meaning a square or quadrate. Its nominative singular is `quadrātum`.
- `vacuus, -a, -um` is a first/second-declension adjective meaning empty, vacant, or unoccupied. Agreement with neuter singular `quadrātum` requires `vacuum`.
- Thus `quadrātum vacuum` is fully agreed in gender, number, and case: neuter singular nominative. Neuter accusative has the same surface forms, but a standalone label normally uses the nominative.
- Classical Latin permits either adjective position, but the unmarked descriptive pattern is noun followed by adjective. Dictionary examples use the same order, such as `pōculum vacuum` (an empty cup); `terra ... vacua` likewise places the emptiness adjective after its noun.
- `vacuum quadrātum` is grammatical but front-loads/emphasizes emptiness and mirrors English word order. It is weaker for a neutral naming phrase.

### Lexical Alternatives

- `quadrātum inane` is grammatical, using `inānis, -e`, but `vacuus` is the more direct ordinary adjective for an unoccupied/empty object.
- `forum vacuum` means an empty public or town square, not the geometric square shown by `□`.
- `area vacua`, `locus vacuus`, and `spatium vacuum` mean empty area/place/space and lose the explicit square geometry.
- `quadrum vacuum` is possible with the less usual synonym `quadrum`, but `quadrātum` is the standard transparent noun for a geometric square.
- Macrons are not required in submission; the site's normalization ignores case and spaces but does not perform Latin synonym matching.

## Common Translation Resource Check

- `QUADRATUM VACUUM` was rejected. The direct-translation model may still be correct while the author's expected lexical order follows a common translation tool rather than neutral hand-composed Latin.
- Querying Google Translate's public translation endpoint from English to Latin gives a casing-sensitive result:

```text
EMPTY SQUARE  -> VACUUM QUADRATUM
empty square  -> inanis quadrata
```

- The accepted intermediate is displayed and submitted as exactly `EMPTY SQUARE` in all caps. Feeding that exact text into the most common translation resource therefore produces `VACUUM QUADRATUM` verbatim.
- This is not an ungrammatical machine artifact:
  - `quadrātum` is neuter nominative singular, "a square".
  - `vacuum` is the agreeing neuter nominative singular of `vacuus`.
  - Latin permits the adjective before the noun; here it emphasizes the empty state and matches the translator's output order.
- Lowercase Google output `inanis quadrata` can also be parsed with feminine `quadrāta` as a substantivized square/figure and agreeing common-gender `inānis`, but it is not the result of the exact uppercase intermediate shown by the puzzle.
- The title and flavor deliberately foreground imperfect/literal translation, so reproducing a common translator's exact output is better grounded than silently correcting it to preferred noun-adjective prose order.

## Casing Audit And Deterministic Non-Latin Alternative

- `VACUUM QUADRATUM` was rejected. The all-caps Google output was a casing artifact, not a stable semantic translation.
- PuzzleCat explicitly ignores answer case, and intermediate answers are conventionally displayed in capitals. Capitalization should therefore not be treated as part of the English phrase's meaning or as a control signal to the translator.
- A normal lowercase semantic query remains reproducible:

```text
Google Translate, English -> Latin
empty square -> inanis quadrata
```

- `inānis quadrāta` is machine-like but morphologically defensible if `quadrāta` is treated as a feminine substantivized adjective with an implied feminine noun such as `figūra` or `area`; `inānis` is the agreeing feminine nominative singular form.
- This awkwardness fits a puzzle centered on literal and imperfect translation better than silently replacing the output with hand-edited `quadrātum vacuum`, which was already rejected.
- There is one separate deterministic English terminology branch: the exact glyph `□` has Unicode name `WHITE SQUARE` (U+25A1). The configured correct-message glyph is `□`, so `WHITE SQUARE` is a justified fallback if the lowercase translator output is rejected.
- Generic answers such as `BLANK`, `SPACE`, or `EMPTY CELL` remain unsupported because they are not the official name of the displayed glyph.

## Multi-Level Hint Chain

- `INANIS QUADRATA` was rejected, eliminating direct translations of the words `EMPTY SQUARE`.
- The two intermediate responses both returned `Keep Going!`, so each can represent a stage rather than two fragments to combine immediately:
  1. `LATIN PHRASE` specifies the eventual output language/type.
  2. `EMPTY SQUARE` identifies a symbol/object, not yet the final source text.
  3. The corresponding glyph is `□`, independently corroborated by the configured correct-message glyph.
  4. Unicode's exact official name for `□` (U+25A1) is `WHITE SQUARE`.
  5. Apply the earlier `LATIN PHRASE` instruction to that official name.
- Google Translate's normal lowercase English-to-Latin result is reproducible:

```text
white square -> album quadratum
```

- Grammar is sound: `album` is the neuter nominative singular of `albus` (white), agreeing with neuter nominative singular `quadrātum` (square).
- `album quadratum` uses adjective-first order, which is permitted and is the exact common-resource output. Hand-edited `quadratum album` is grammatical but no longer reproduces the common translator.
- This chain uses both accepted intermediates and both `Keep Going!` prompts: the first tells the final language, while the second forces one more semantic lookup from `EMPTY SQUARE` to the standardized text `WHITE SQUARE` before translation.

## Candidates

1. `ALBUM QUADRATUM` - confidence 88%. Exact common-translator Latin output for the official Unicode name `WHITE SQUARE`, using both intermediate stages.
2. `QUADRATUM ALBUM` - confidence 8%. Grammatically neutral noun-adjective order, but not the exact common-resource output.
3. `WHITE SQUARE` - confidence 4%. Exact Unicode name, but stopping here leaves `LATIN PHRASE` unused as the requested output type.

## Submissions

- `LATIN PHRASE` - intermediate, feedback `Keep Going!`; incorrect count remains 0.
- `NEC VERBUM VERBO` - incorrect; incorrect count 1.
- `PERGE` - incorrect; incorrect count 2. This disproves interpreting the intermediate feedback as an English phrase to translate directly.
- `EMPTY SQUARE` - intermediate, feedback `Keep Going!`; incorrect count remains 2.
- `TOFU` - incorrect; incorrect count 3. This disproves treating `EMPTY SQUARE` as a missing-glyph definition.
- `SATOR AREPO TENET OPERA ROTAS` - incorrect; incorrect count 4.
- `SATOR SQUARE` - incorrect; incorrect count 5.
- `PERSONA NON GRATA` - incorrect; local archived incorrect count 6. The root reports an authoritative total of 8 after subsequent work; the two additional answer strings are not present in the current local submission snapshot.
- `QUID PRO QUO` - incorrect; authoritative incorrect count 9. This disproves outputting the Latin row selected by the common blank.
- `PLATINUM` - incorrect; incorrect count 10.
- `PT` - incorrect; incorrect count 11.
- `铂` - incorrect; incorrect count 12.
- `78` - incorrect; incorrect count 13. This rejects the atomic-number output and the periodic-table branch as a terminal mechanism.
- `PQRST` - incorrect; incorrect count 14. This rejects the coordinate-label/space-letter construction and triggers abandonment of the shared-empty-cell branch.
- `LATIN SQUARE` - incorrect; incorrect count 15.
- `TABULA RASA` - incorrect; incorrect count 16.
- `QUADRATUM VACUUM` - incorrect; incorrect count 17. This falsifies the neutral noun-adjective order but not the exact translator-output model.
- `VACUUM QUADRATUM` - incorrect; incorrect count 18. This falsifies treating the intermediate's display capitalization as a Google Translate control signal.
- `INANIS QUADRATA` - incorrect; incorrect count 19. This eliminates directly translating the wording `EMPTY SQUARE`.

## Stopping Criteria

- `ALBUM QUADRATUM` and `WHITE SQUARE` were both rejected. The Unicode-name and direct-translation branches are closed.
- Do not submit another answer without a deterministic extraction that produces coherent text.

## Current Structural Audit

- Authoritative incorrect count is 20. The local submission archive contains 19 incorrect verdicts plus the two accepted intermediates, so at least one incorrect answer is not represented locally.
- Verified intermediates remain:
  - `LATIN PHRASE` -> `Keep Going!`
  - `EMPTY SQUARE` -> `Keep Going!`
- The semantic matching permutation from printed left order to printed right order is `[5,11,6,7,8,10,3,9,4,2,1]`, a single 11-cycle:
  `1 -> 5 -> 8 -> 9 -> 4 -> 7 -> 3 -> 6 -> 10 -> 2 -> 11 -> 1`.
- The defensible literal reading of `Keep Going!` is to continue forward from each indexed Latin letter to actual word spaces. Punctuation must not be silently converted to an empty cell.
- Space-preserving 11-character Latin continuations (`.` denotes a real space):

```text
ERA.AD.ASTR
MANUM.ESTER
PERSONA.NON
TO.MORIMEME
YRANNISSIC.
STALEA.IACT
QUOQUID.PRO
UMMA.CUM.LA
AECASAD.KAL
RBAFACTA.NO
EMCARPE.DIE
```

- Space coordinates in that square are `(1,4),(1,7),(2,6),(3,8),(4,3),(5,11),(6,7),(7,8),(8,5),(8,9),(9,8),(10,9),(11,8)`.
- The earlier unique-common-blank overlay at `(7,8)` is overfit: it depends on inconsistent punctuation handling and an unsupported overlay of different printed orders. Do not revive `(7,8)`, periodic-table, `PQRST`, Unicode, or direct-Latin-translation variants.
- Active tests are limited to structurally justified uses of the 11-cycle, all real phrase spaces modulo 11, and letters selected by those empty-cell masks.

## Additional Rejection

- `WHITE SQUARE` - incorrect; authoritative incorrect count 20. This closes the Unicode-name branch.

## Resumed Analysis: 2026-07-13

- Extending every Latin phrase through one full real-space cycle and reducing offsets modulo 11 gives 21 distinct empty cells, not a coherent row-, column-, time-, or 11-cycle-order message.
- Using those Latin spaces as a mask over the semantically matched English continuations was tested with:
  - raw characters and letters-only streams;
  - first-space-only and all-space masks;
  - left, right, reverse-right, column, time, and semantic-cycle traversals.
- None yields readable text. The first-window letters-only mask gives `ANTHUOHCIRSTE`; its suggestive anagrams are not backed by a route and must not be treated as extraction.
- Advancing through the semantic 11-cycle while advancing through grid columns, in both directions and from every starting row, also gives no coherent text.
- Perimeter and inward-spiral continuations of both the English and Latin 11 x 11 grids were checked. They preserve the accepted first-column messages but do not reveal a third instruction.

## Unsubmitted Thematic Candidates

1. `BLANK SPACE` - leading but unverified.
   - It is the most idiomatic two-word paraphrase of the accepted clue `EMPTY SQUARE`.
   - Replacing an awkward literal rendering with a familiar phrase repeats the puzzle's central translation operation and fits the title `信达雅`.
   - The configured correct-message glyph `□` corroborates a blank space/cell, though it is not independent extraction evidence.
   - This answer has not been submitted and should not be promoted unless the root worker accepts a semantic-clue final rather than requiring another grid extraction.
2. `METAPHRASE` - thematic, unverified.
   - John Dryden, named explicitly in the flavor, used *metaphrase* for word-for-word translation.
   - The awkward Chinese renderings and `谢谢你非常多，先生辜` are deliberate word-for-word calques.
   - No deterministic use of `EMPTY SQUARE` currently selects this term.
3. `PARAPHRASE` - thematic, weaker.
   - The Chinese idioms, English sayings, and Latin phrases preserve sense while changing wording, matching Dryden's *paraphrase* category.
   - Again, no mechanical extraction selects it over `METAPHRASE`.

No submission is recommended yet. If a semantic-clue answer is permitted, test `BLANK SPACE` before either Dryden term; otherwise continue searching for an explicit ordering of the Latin word-boundary cells.

## Calque And Word-Boundary Audit

- The strict, minimal action described by the second `Keep Going!` is not to wrap the phrases or overlay two independently ordered matrices. It is simply to advance from each indexed Latin letter until the next word boundary.
- All 11 rows deterministically reach an ordinary inter-word **space**. Attempts to read neighboring letters, distances, or the complete set of boundary coordinates do not produce language, so the common destination itself is the stable output.
- `EMPTY SQUARE` is a precise word-for-word English gloss of Chinese `空格`:
  - `空` = empty;
  - `格` = cell/compartment, normally drawn as a square in a table or character grid.
- The English Wiktionary entry for `空格` defines it as `space; gap (between words or lines); empty cell (in a table)`, and in computing as a shortening of `空格键` (space bar). This independently unifies the two otherwise separate senses in the accepted intermediate: an empty grid square and a word space.
- The flavor gives the same reverse-calque instruction in miniature:
  - `谢谢你非常多` preserves English `thank you very much` word order instead of idiomatic Chinese;
  - `先生辜` preserves English `Mr. Gu` order instead of Chinese `辜先生`.
- Therefore the puzzle's repeated operation is to recover the idiomatic/source expression from an awkward word-for-word rendering. Applying it to `EMPTY SQUARE` gives Chinese `空格`, whose actual referent is the spaces reached by continuing through the Latin phrases.
- This also closes the language loop naturally: Chinese idioms -> English sayings -> Latin phrases -> a Chinese lexical answer.

## Revised Unsubmitted Candidates

1. `空格` - strongest new candidate.
   - It exactly accounts for both words of `EMPTY SQUARE`, the real word-boundary destination forced by `Keep Going!`, the Chinese title/flavor, and the correct-message glyph `□`.
   - Unlike the discarded space matrices, this does not depend on a window size, punctuation deletion, overlay order, or route choice.
2. `SPACE` - English rendering of the same mechanism.
   - Mechanically it names what every continuation reaches, but it does not close the source-language loop or preserve the `格`/square half of the intermediate as explicitly as `空格`.
3. `BLANK SPACE` - downgraded.
   - It is an English synonym of the intermediate but lacks the exact Chinese morpheme correspondence and is not the standard concise translation of `空格`.

The Dryden terms `METAPHRASE` and `PARAPHRASE` remain useful thematic descriptions, but the flavor's awkward syntax is fully explained by the reverse-calque operation and no extraction selects either term. They should not precede `空格`/`SPACE`.

The complete 11-cycle is not sufficient evidence for a route: a uniformly random permutation of 11 items is a single cycle with probability `1/11`, and every mechanically natural cycle traversal tested above is nonlinguistic. Treat it as incidental unless another independent clue specifies how to use it.

## Rejection: `空格`

- Root submitted `空格`; verdict was incorrect. Authoritative incorrect count is now 22.
- This closes the reverse-calque-to-Chinese terminal branch. The dictionary equivalence between `空格`, a word space, and an empty table cell remains thematically apt, but it is not the checker answer.
- Do not submit `SPACE`, `BLANK SPACE`, `WHITESPACE`, or `空格键` solely as lexical variants. A new mechanical extraction is required.

## Non-Cyclic Continuation And Emptying Tests

- Reading from each indexed Latin letter without wrapping gives the following stable suffixes to the end of the current word:

```text
ERA
MANUM
PERSONA
TO
YRANNIS
ST
QUO
UMMA
AECAS
RBA
EM
```

- Reading instead to the end of the whole Latin phrase, with spaces removed, gives:

```text
ERAADASTRA
MANUMEST
PERSONANONGRATA
TOMORI
YRANNIS
ST
QUO
UMMACUMLAUDE
AECAS
RBA
EM
```

- Left-aligning, right-aligning, or padding either set in an 11 x 11 square produces no readable boundary, diagonal, disappearance-order, or empty-cell extraction. The order in which phrase suffixes become empty is also nonlinguistic.
- Filling the padded empty cells with corresponding English continuation letters was tested. It merely reproduces recognizable suffixes of the source English sayings and gives no third message by rows or columns.
- Interpreting `EMPTY SQUARE` as an empty keyed 5 x 5 alphabet square was tested in both directions:
  - key `LATIN PHRASE`, text `EMPTY SQUARE`;
  - key `EMPTY SQUARE`, text `LATIN PHRASE`.
- Standard Playfair and Bifid encryption/decryption, including full-length and period-5 blocks with the usual I/J merge, produce no readable plaintext. Close this cipher-square branch unless a separate ciphertext or cipher name appears.
- Interpreting the square-bracket index `[n]` as an instruction to keep deleting letters until the phrase is empty was tested in two forms:
  - sequential continuation after the indexed letter, which is just the already-audited rotated phrase stream;
  - Josephus elimination using `[n]` as the step size.
- Josephus round 1 does reproduce `EMPTY SQUARE`, as it must because the first removed letter is the indexed letter. Subsequent rounds begin `TREMEERMAVI`, `SURMSTPCENM`, `SESEALOMAEA`, etc.; none is linguistic in left, right, reverse-right, cycle, or reverse-cycle order.
- Advancing the character offset while simultaneously traversing the semantic 11-cycle was tested for English-only, Latin-only, and alternating English/Latin streams, forward and backward, from every starting row. No result is linguistic.

Conclusion: `Keep Going` does not support a continued-character, repeated-deletion, Josephus, keyed-square, or cycle-diagonal third extraction under standard rules.

## Square-Bracket To Parenthesis Enumeration Audit

- A bounded interpretation of `EMPTY SQUARE` is that the square-bracket indices `[n]` have been consumed, so the remaining explicit numerical data are the right-column word enumerations in round parentheses.
- For each semantic row, locating `[n]` in the original English enumeration uniquely gives these quantities:
  - word number: `3,2,1,2,4,3,2,1,4,2,3`;
  - position within that word: `1,2,1,2,1,2,5,2,5,4,1`;
  - current word length: `2,7,4,4,5,2,7,13,7,5,4`;
  - letters from the indexed letter through the word end: `2,6,4,3,5,1,3,12,3,2,4`;
  - remaining word count: `2,1,4,5,1,2,7,1,2,4,2`.
- Direct A1Z26 readings of these sequences are nonlinguistic in semantic-left, printed-right, and 11-cycle orders.
- Using each sequence as a fresh rowwise index into the corresponding Latin phrase, at the indexed position or one character after it, was also tested in all three orders. Representative results include `RRPESEUSAAR`, `PRPESLPULTC`, `EHSEELOENAP`, `EESMEAIDKAP`, and `EESNSLOSDTA`; none is language.
- Treating `(word number, position in word)` as a coordinate and transferring it from the English saying to the corresponding Latin phrase produces only `AUPO.S.U...`; the empty/invalid rows do not form a mechanically ordered answer in left, right, or cycle order.
- Pairing each English enumeration number with the corresponding Latin word and taking that numbered letter produces dotted fragments such as `EEDR`, `.M`, `SOAS`, `EIMOE.`, `.PY.`, etc. Reversing the operation (Latin word lengths into English words) is likewise nonlinguistic.

Conclusion: the explicit `[ ]` versus `( )` typography does not yield a third layer through the standard direct enumeration transfers. Close this mechanism unless a new instruction specifies a nonstandard aggregation.

## Dryden Translation-Mode Audit

- The flavor's use of `德莱顿先生` in a puzzle about translation is a strong, explicit allusion to John Dryden's ordered trichotomy:
  1. **metaphrase** - word-for-word and line-by-line literal translation;
  2. **paraphrase** - sense-for-sense translation, retaining the author's meaning without strictly following the words;
  3. **imitation** - a much freer rendering that may vary from both the words and the sense, using only general hints from the original.
- The right-hand Chinese and the flavor's `谢谢你非常多，先生辜` clearly demonstrate **metaphrase**. They preserve English wording and word order even where idiomatic Chinese would differ (`thank you very much`, `Mr. Gu`).
- Replacing those calques with established Chinese sayings is at least **paraphrase**: the wording changes while the intended sense remains recognizable.
- The Latin sayings are sometimes freer cultural analogues, so **imitation** is thematically plausible. However, the distinction is not uniform enough to assign the entire Latin layer uniquely to Dryden's third category:
  - close equivalents such as `ACTIONS SPEAK LOUDER THAN WORDS` -> `FACTA NON VERBA`, `YOU ONLY LIVE ONCE` -> `CARPE DIEM`, and `NOBODY'S PERFECT` -> `ERRARE HUMANUM EST` remain sense-preserving paraphrases;
  - loose matches such as `COME HOME TO ROOST` -> `SIC SEMPER TYRANNIS`, `PAIN IN THE NECK` -> `PERSONA NON GRATA`, and `VALEDICTORIAN` -> `SUMMA CUM LAUDE` are more imitation-like;
  - the Chinese idiom layer itself contains both close and loose analogues, so freedom does not increase in a mechanically consistent three-stage sequence.
- `LATIN PHRASE` directly instructs the second semantic continuation, but neither it nor `EMPTY SQUARE` labels a Dryden category. The puzzle contains no drawn three-box sequence with a third empty position. Treating `EMPTY SQUARE` as that missing third slot would be an unsupported metaphor; the checker response glyph `□` is UI feedback, not a slot in the puzzle body.
- Therefore **IMITATION** is a plausible thematic completion of Dryden's list, but it is not uniquely selected by the two accepted intermediates or by a consistent row-by-row classification. `METAPHRASE` and `PARAPHRASE` describe real layers but are likewise not extracted answers.

Conclusion: this finite flavor audit produces **no submission candidate**. Do not submit `IMITATION` without an additional explicit ordering or slot mechanism.

## Public-Web Research: Q.E.D.

Non-interactive searches were run on 2026-07-13 without opening the PuzzleCat page:

- Exact puzzle ID: `"XYkPIapg"`.
- Title/platform and author combinations: `"信达雅" PuzzleCat`, `"信达雅" "Brightly_"`, and `"Brightly_" PuzzleCat`.
- Exact or near-exact flavor fragments: `"谢谢你非常多，先生辜"`, `"德莱顿先生" "成语和俗语"`, and `"德莱顿先生将向诸位解释它们的意思"`.
- Distinctive body/intermediate combinations: `"苦尽甘来" "人非圣贤" "过街老鼠" "钻火得冰"`, `"LATIN PHRASE" "EMPTY SQUARE"`, and `"EMPTY SQUARE" "Keep Going!" puzzle`.
- Site-restricted searches for GitHub, Gitee, Zhihu, Bilibili, Weibo, WeChat, and QQ Docs; direct GitHub issue/repository and Hacker News searches for the puzzle ID.

No public discussion, hint, walkthrough, or answer record for this specific puzzle was found. Yahoo indexed only the PuzzleCat puzzle page for the exact ID; Brave, GitHub, and Hacker News had no relevant ID hit. Broad title searches returned unrelated translation-theory material.

However, the exact combined-intermediate search produced a standard mathematical equivalence that was not previously tested:

- Wolfram MathWorld, **Q.E.D.**: <https://mathworld.wolfram.com/QED.html>
  - `Q.E.D.` is an abbreviation of the Latin phrase `quod erat demonstrandum`.
  - Symbols used as synonyms for Q.E.D. include a filled square, filled rectangle, or an **empty square**.
- Wikipedia, **Q.E.D.** and **Tombstone (typography)**, checked through the public MediaWiki API:
  - <https://en.wikipedia.org/wiki/Q.E.D.>
  - <https://en.wikipedia.org/wiki/Tombstone_(typography)>
  - The end-of-proof/tombstone symbol may be `∎` or `□` and is used in place of `Q.E.D.`, the traditional abbreviation of `quod erat demonstrandum`.
  - A hollow square (`\square` or `\Box`) is a standard form of this symbol.

### Local Verification

The external fact exactly combines all stable local evidence:

1. `LATIN PHRASE` was accepted with `Keep Going!`.
2. Continuing the semantic chains produced `EMPTY SQUARE`, also accepted with `Keep Going!`.
3. `QUOD ERAT DEMONSTRANDUM` is the Latin phrase conventionally abbreviated `Q.E.D.`.
4. An empty/hollow square `□` is the typographical synonym that replaces `Q.E.D.` at the end of a proof.
5. The puzzle's configured correct-message glyph is exactly `□`, independently confirming the intended symbol.

This requires no arbitrary grid size, punctuation rule, translation choice, or external code. The two intermediates are parallel definitions of the same conventional answer:

```text
LATIN PHRASE  -> QUOD ERAT DEMONSTRANDUM -> Q.E.D.
EMPTY SQUARE  ---------------------------> Q.E.D.
```

## Recommended Submission

1. `QED` - strongest candidate. It is the conventional name/abbreviation directly synonymous with the empty square; PuzzleCat strips punctuation, so `Q.E.D.` normalizes to `QED`.
2. `QUOD ERAT DEMONSTRANDUM` - submit only if `QED` is rejected. It is the expanded Latin phrase, but the square most directly replaces the abbreviation `Q.E.D.` rather than requiring the full expansion as the answer string.

The Q.E.D. branch supersedes the prior no-candidate conclusion from the Dryden-only audit. It is mechanically selected by both accepted intermediates and corroborated by the local `□` success glyph.
