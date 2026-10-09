# Aptitude Round — Preparation Guide

## 1. What Recruiters Evaluate in an Aptitude Test

- **Speed & accuracy** — most tests are timed (45–90s/question), so recruiters filter for both.
- **Fundamentals** — school-level math and logic, tested under time pressure, not advanced theory.
- **Pattern recognition** — series, puzzles, DI all reward spotting the underlying rule fast.
- **Elimination skill** — MCQ format rewards ruling out wrong options over solving from scratch.
- **Consistency across sections** — most companies set a **sectional cutoff** (Quant / Logical / Verbal), so you can't skip a weak section and coast on a strong one.

---

## 2. Overall Structure

Most campus/off-campus aptitude tests (TCS NQT, Infosys, Wipro, Amcat, Cocubes, etc.) have 3 sections:

| Section | Typical Subtopics | Weight |
|---|---|---|
| **Quantitative Aptitude** | Arithmetic, Algebra, Geometry, DI | ~40% |
| **Logical Reasoning** | Series, arrangements, coding, puzzles | ~35% |
| **Verbal Ability** | Grammar, RC, vocabulary | ~25% |

---

## 3. Subtopics by Difficulty

### 3.1 Quantitative Aptitude

| Difficulty | Subtopics |
|---|---|
| **Easy** | Number System (LCM/HCF, divisibility), Percentages, Averages, Ratio & Proportion, Simple Interest |
| **Medium** | Profit & Loss, Compound Interest, Time & Work, Time-Speed-Distance, Mixtures & Alligation, Ages |
| **Hard** | Permutation & Combination, Probability, Data Interpretation (multi-step), Algebra (quadratic/progressions), Mensuration (3D solids), Boats & Streams (relative-speed variants) |

### 3.2 Logical Reasoning

| Difficulty | Subtopics |
|---|---|
| **Easy** | Number/Letter Series, Coding-Decoding, Blood Relations, Direction Sense |
| **Medium** | Syllogisms, Venn Diagrams, Clocks & Calendars, Analogy, Odd One Out |
| **Hard** | Seating Arrangement (linear/circular), Puzzles (grid-based), Data Sufficiency, Statement-Conclusion/Assumption |

### 3.3 Verbal Ability

| Difficulty | Subtopics |
|---|---|
| **Easy** | Synonyms/Antonyms, One-word Substitution, Spotting Errors |
| **Medium** | Sentence Correction, Fill in the Blanks, Prepositions/Tenses |
| **Hard** | Para Jumbles, Reading Comprehension (inference-based), Critical Reasoning/Verbal Analogy |

---

## 4. Quantitative Aptitude — Formulae, Tricks & Patterns

### Number System
- **Formulae**: LCM × HCF = product of two numbers. Divisibility: by 3/9 → digit sum; by 11 → alternating digit-sum difference.
- **How to apply**: Break numbers into prime factors first — almost every LCM/HCF/divisibility question collapses to factorization.
- **Tips**: Memorize squares (1–30), cubes (1–15), and prime numbers up to 100 — saves 10–15s per question.
- **Common pattern**: "Find the smallest number that leaves remainder r when divided by a, b, c" → LCM(a,b,c) + r.

### Percentages
- **Formulae**: `% change = (New − Old)/Old × 100`. Successive % change: `a + b + ab/100`.
- **How to apply**: Convert percentages to fractions (25% = 1/4, 33.33% = 1/3, 12.5% = 1/8) — multiplying fractions is faster than decimals.
- **Tips**: If a value increases by x% then decreases by x%, net effect is always `−x²/100` (a loss).
- **Common pattern**: Population/price increase-decrease chains — use successive-change formula instead of computing each step.

### Averages
- **Formulae**: `Average = Sum/Count`. If one value is replaced, `new sum = old sum − removed + added`.
- **How to apply**: For "average age of group" problems, work with the **sum**, not the average, until the final step.
- **Tips**: Average of consecutive numbers = middle term (or mean of first & last).
- **Common pattern**: "A new person joins and average changes by x" → set up sum equations, solve for the unknown directly.

### Ratio & Proportion
- **Formulae**: `a:b = c:d ⇒ ad = bc`. Combining ratios: convert to a common term (LCM of the shared quantity).
- **How to apply**: Express everything as parts of a whole (e.g., 2:3:5 → total 10 parts) rather than converting to actual values early.
- **Tips**: In mixture/ratio-of-shares problems, keep answers in "parts" as long as possible — reduces arithmetic errors.
- **Common pattern**: Partnership problems (profit split by capital × time) reduce to a ratio question.

### Simple Interest (SI) & Compound Interest (CI)
- **Formulae**: `SI = PRT/100`. `CI = P(1 + R/100)^T − P`. `CI − SI (for 2 yrs) = P(R/100)²`.
- **How to apply**: For CI over 2 years, use the shortcut `CI − SI = P×(R/100)²` instead of computing compound amount fully.
- **Tips**: Effective rate for half-yearly compounding = `R/2` for `2T` periods.
- **Common pattern**: "Difference between CI and SI for 2/3 years" — always solvable via the shortcut, never brute-force the compound formula.

### Profit & Loss
- **Formulae**: `Profit% = (SP−CP)/CP × 100`. `SP = CP(1 ± %/100)`. Marked price: `SP = MP(1 − discount%/100)`.
- **How to apply**: Assume CP = 100 for percentage-only problems — turns every answer into a direct percentage.
- **Tips**: Successive discounts combine like successive percentage changes: `a + b − ab/100` (note the sign flips for discounts vs. gains).
- **Common pattern**: False weight problems → `Profit% = (True value − False value)/False value × 100`.

### Time & Work
- **Formulae**: If A does a job in `n` days, A's 1-day work = `1/n`. Combined work = sum of individual rates.
- **How to apply**: Assume total work = LCM of the given days — converts fractions into whole "units of work per day," which is far faster than fraction arithmetic.
- **Tips**: "A is twice as efficient as B" → A's days = B's days / 2 (efficiency and time are inversely proportional).
- **Common pattern**: Pipes & cisterns is Time & Work with negative rates (outlet pipes subtract from the work rate).

### Time, Speed & Distance
- **Formulae**: `Speed = Distance/Time`. `km/h → m/s`: multiply by `5/18` (and reverse by `18/5`). Relative speed: same direction → subtract; opposite → add.
- **How to apply**: For train problems, always add the train's own length to the distance when it "crosses" a platform or another object.
- **Tips**: Average speed for equal distances at speeds `a` and `b` = `2ab/(a+b)` (harmonic mean, NOT arithmetic mean) — a very common trap.
- **Common pattern**: Boats & streams: downstream speed = `b+s`, upstream = `b−s`; boat speed = avg of the two, stream speed = half the difference.

### Mixtures & Alligation
- **Formulae**: Alligation rule: `(Quantity of cheaper)/(Quantity of dearer) = (Dearer price − Mean price)/(Mean price − Cheaper price)`.
- **How to apply**: Draw the alligation cross (cheaper value, dearer value, mean in the middle) — visual method beats algebra here.
- **Tips**: Repeated dilution ("replace x liters of mixture with water, n times"): `Final conc. = Initial × (1 − x/V)^n`.
- **Common pattern**: Mixing two solutions to hit a target ratio/concentration — always alligation, rarely simultaneous equations.

### Ages
- **Formulae**: No fixed formula — set up linear equations from "x years ago / y years hence" statements.
- **How to apply**: Assign one variable to the present age of the key person; express everyone else relative to it.
- **Tips**: Re-read the tense carefully — "was" (past), "will be" (future), "is" (present) each shift the equation differently.
- **Common pattern**: Ratio-of-ages-then-and-now — set present ages as `kx, ky`, apply the "n years ago/hence" condition, solve for `k`.

### Permutation & Combination
- **Formulae**: `nPr = n!/(n−r)!` (order matters). `nCr = n!/(r!(n−r)!)` (order doesn't matter). Circular arrangements: `(n−1)!`.
- **How to apply**: Ask "does order matter?" first — that single question decides P vs. C.
- **Tips**: For "at least one" / "at least 2 vowels together" type constraints, compute total − complement (unwanted case) rather than direct casework.
- **Common pattern**: Group photo / seating with restrictions ("A and B must sit together") → treat the pair as one block, arrange, then multiply by internal arrangements (2! for the pair).

### Probability
- **Formulae**: `P(event) = Favorable outcomes/Total outcomes`. `P(A or B) = P(A)+P(B)−P(A∩B)`. `P(A and B, independent) = P(A)×P(B)`.
- **How to apply**: Enumerate the sample space explicitly for small cases (dice, cards) before reaching for a formula — reduces setup errors.
- **Tips**: "At least one" probability = `1 − P(none)` — almost always the fastest route.
- **Common pattern**: Cards/dice combined events — break into independent sub-events, multiply, then sum over valid cases.

### Algebra (Quadratics, Progressions)
- **Formulae**: Quadratic roots: `x = [−b ± √(b²−4ac)]/2a`. Sum of roots `= −b/a`, product `= c/a`. AP: `Tn = a+(n−1)d`, `Sn = n/2[2a+(n−1)d]`. GP: `Tn = ar^(n−1)`, `Sn = a(r^n−1)/(r−1)`.
- **How to apply**: For "sum of roots / product of roots" questions, skip solving the quadratic entirely — use the `−b/a`, `c/a` shortcuts.
- **Tips**: Recognize AP vs. GP fast: constant difference → AP; constant ratio → GP.
- **Common pattern**: "Find nth term given two other terms" — set up two equations in `a` and `d` (or `a` and `r`), solve simultaneously.

### Mensuration
- **Formulae**: Cylinder: `V = πr²h`. Cone: `V = ⅓πr²h`. Sphere: `V = 4/3πr³`. Cuboid: `V = l×b×h`. Surface areas follow the standard set (curved/total surface area per solid).
- **How to apply**: Keep a one-page formula sheet of 2D (area/perimeter) and 3D (volume/surface area) shapes — mensuration is pure recall + substitution, no "trick" replaces knowing the formula.
- **Tips**: Watch units — mixed cm/m in the same question is the most common careless-error trap.
- **Common pattern**: "Melt and recast" problems (e.g., sphere melted into cylinders) → equate volumes, solve for the unknown dimension.

### Data Interpretation (DI)
- **Formulae**: No new formulae — DI tests speed applying percentage, ratio, and average formulae to tables/graphs/pie charts.
- **How to apply**: Skim the chart's title, axes, and units first (10 seconds) before reading any question — prevents misreading the data under time pressure.
- **Tips**: For pie charts, convert % directly to degrees (`% × 3.6`) only if the question asks for angle; otherwise work in %.
- **Common pattern**: "Approximate value" questions — round aggressively (e.g., 48.7% → ~50%) since options are usually far apart.

---

## 5. Logical Reasoning — Formulae, Tricks & Patterns

### Number/Letter Series
- **Rule types**: arithmetic difference, geometric ratio, alternating pattern, difference-of-differences, squares/cubes ± constant.
- **How to apply**: Check differences between consecutive terms first; if not constant, check the differences of differences (second order) or ratios.
- **Tips**: For letter series, convert letters to numbers (A=1...Z=26) mentally, spot the numeric pattern, convert back.
- **Common pattern**: Two interleaved series (odd positions follow one rule, even positions another) — split the series into two sub-series first.

### Coding-Decoding
- **Rule types**: letter-shift ciphers, number coding, substitution coding.
- **How to apply**: Find the shift/rule using the given example pair, then apply the exact same rule mechanically to the new word — don't re-derive logic per letter.
- **Tips**: Write the alphabet with position numbers (1–26) on scratch paper once; reuse it for every coding question in the section.
- **Common pattern**: "If CAT is coded as XZG, how is DOG coded?" → each letter maps to `(27 − position)`; apply identically.

### Blood Relations
- **How to apply**: Draw a family tree as you read each clue — never try to hold relations in your head.
- **Tips**: Use `+` for male, `−` for female, and standard symbols (↑ for parent-of, → for spouse) for speed.
- **Common pattern**: "Pointing to a photograph..." puzzles — resolve pronouns (his/her) to a specific person on the tree before answering.

### Direction Sense
- **Formulae**: Standard compass turns — right turn from North → East → South → West → North (clockwise); left turn is the reverse.
- **How to apply**: Sketch a simple x-y grid; plot each move as a coordinate change (N/S = y-axis, E/W = x-axis) and track net displacement.
- **Tips**: Final distance from start = Pythagorean distance between the start point and end point on your grid, not the sum of the paths walked.
- **Common pattern**: "Shortest distance to return to start" — always the straight-line (hypotenuse) distance.

### Syllogisms
- **Rule types**: All/Some/No statements; validity via Venn diagram overlap.
- **How to apply**: Draw Venn circles for each statement; a conclusion is valid only if it holds in **every** possible diagram consistent with the premises, not just one.
- **Tips**: "Some A are B" does NOT imply "Some A are not B" — a classic trap; check each conclusion independently.
- **Common pattern**: Two premises sharing a common (middle) term → conclusion links the two outer terms only if the middle term is "distributed" (i.e., "All" or "No", not "Some").

### Venn Diagrams
- **Formulae**: `|A∪B| = |A|+|B|−|A∩B|`; for three sets, `|A∪B∪C| = |A|+|B|+|C|−|A∩B|−|B∩C|−|A∩C|+|A∩B∩C|`.
- **How to apply**: Fill the diagram from the innermost region (all three overlapping) outward — prevents double-counting.
- **Tips**: Label each region with its exact count as you compute it; the outer "none of the above" region is often what's asked.
- **Common pattern**: "How many students play exactly one/two sports" — read "exactly" vs. "at least" carefully; they use different regions.

### Clocks & Calendars
- **Formulae**: Minute hand moves `6°/min`; hour hand moves `0.5°/min`. Angle between hands = `|30H − 5.5M|`. Odd days: 1 ordinary year = 1 odd day, leap year = 2 odd days.
- **How to apply**: For "day of the week" problems, compute total odd days from the reference date and map `0–6` to Sun–Sat.
- **Tips**: Hands overlap every `65 5/11` minutes, not exactly every hour — memorize this constant.
- **Common pattern**: "At what time between H and H+1 will the hands be at angle θ" → solve `|30H − 5.5M| = θ` for `M`.

### Analogy & Odd One Out
- **How to apply**: State the relationship of the given pair in a short sentence ("X is a part of Y", "X is used to make Y") before scanning options — prevents surface-level (same-category-only) matching.
- **Tips**: Watch for relationship *type* changes (part-whole vs. cause-effect vs. synonym) — options often mimic the category but not the relationship.
- **Common pattern**: Odd-one-out among 4 items — 3 share a specific relationship/attribute; the odd one fails exactly one shared criterion.

### Seating Arrangement & Puzzles
- **How to apply**: Process the most restrictive/absolute clues first (exact positions), then relative clues (left of, next to), then eliminate remaining options.
- **Tips**: For circular arrangements, fix one person's position arbitrarily to remove rotational ambiguity before placing others.
- **Common pattern**: Grid/table puzzles (people × attributes) — build a matrix, mark ✓/✗ as clues are processed, most cells resolve via elimination alone.

### Data Sufficiency
- **How to apply**: Evaluate Statement 1 alone, then Statement 2 alone (independently — don't carry information across), then combine only if neither alone suffices.
- **Tips**: The answer often hinges on one edge case (zero, negative number, non-integer) that a statement doesn't rule out — actively hunt for it.
- **Common pattern**: A statement that looks sufficient at a glance is insufficient because it allows multiple values satisfying it — always test with two different numbers before declaring sufficiency.

### Statement–Conclusion / Assumption
- **How to apply**: A "conclusion" must follow logically and only from the statement; an "assumption" is an unstated premise the statement depends on to make sense.
- **Tips**: If negating the assumption makes the original statement's argument fall apart, it's a valid assumption — this negation test is the standard checker.
- **Common pattern**: Over-broad conclusions ("always", "never", "only") are usually wrong even if the statement supports a mild version of the claim.

---

## 6. Verbal Ability — Tips & Patterns

### Synonyms / Antonyms / One-word Substitution
- **How to apply**: Learn words in context (a sentence), not isolated word lists — recall is far stronger with context.
- **Tips**: Build a running list of confusing word pairs (e.g., *affect/effect*, *complement/compliment*) — these recur across tests.
- **Common pattern**: Distractor options are often near-synonyms with a subtly different connotation (formal vs. informal, positive vs. negative charge) — eliminate by tone, not just meaning.

### Spotting Errors / Sentence Correction
- **How to apply**: Check in this order — subject-verb agreement → tense consistency → pronoun reference → preposition usage → parallelism.
- **Tips**: Read the sentence once for meaning, then a second time purely scanning grammar — don't do both in one pass.
- **Common pattern**: The error is usually in the part of the sentence that looks unremarkable, not the flashy long clause — test-makers hide errors in plain segments.

### Fill in the Blanks
- **How to apply**: Predict the type of word needed (positive/negative, noun/verb, formal/informal) from context before looking at the options.
- **Tips**: For double-blank questions, eliminate using whichever blank has more clearly distinct options first, then check the remaining pair against the second blank.
- **Common pattern**: Contrast words ("however", "although", "despite") signal the blank should be the *opposite* tone of the surrounding clause.

### Para Jumbles
- **How to apply**: Find the opening sentence (introduces the topic, no pronoun referring backward) and the closing sentence (summarizes/concludes) first; the middle usually falls into place via linking words and pronouns.
- **Tips**: Pronouns ("this", "it", "they") and connectors ("therefore", "but", "similarly") are the glue — trace what each pronoun refers to, to fix adjacency.
- **Common pattern**: Two sentences often form an unbreakable pair (cause→effect or claim→example) — spot these pairs first, then place the pair as a unit.

### Reading Comprehension
- **How to apply**: Skim the passage first for structure and tone (30–40s), then read questions, then go back to the relevant paragraph for each answer — don't try to memorize the whole passage.
- **Tips**: For inference questions, the correct option is supported by the passage but never explicitly stated — reject options that quote the passage too literally (often a trap) or add outside information.
- **Common pattern**: "Primary purpose/tone of the passage" questions — answer from the passage as a whole, not from one paragraph.

---

## 7. General Test-Day Tips & Tricks

- **Sectional time budget**: Decide per-section time caps beforehand (e.g., 20 min Quant / 15 min Logical / 15 min Verbal) and stick to it — a jammed question in Quant shouldn't eat into Verbal time.
- **Skip and return**: Mark unfamiliar questions and move on; return only after finishing the confident ones — protects against running out of time on easy points elsewhere.
- **Elimination over derivation**: In MCQs, plugging in the options (especially for algebra/ages/equations) is often faster than solving algebraically from scratch.
- **Approximation is your friend**: When options are far apart (DI, percentages), round numbers aggressively instead of computing exact values.
- **Negative marking awareness**: Check if the test penalizes wrong answers — if so, only guess when you've eliminated at least 1–2 options; if no negative marking, attempt every question.
- **Mock tests > topic drilling alone**: Timed full-length mocks reveal your actual per-section speed and reveal habitual mistakes (silly errors, time sinks) that topic-wise practice won't surface.
- **Keep a formula sheet**: A single page of the shortcuts above (SI/CI, averages, TSD, alligation, nCr/nPr, mensuration) reviewed the morning of the test beats re-deriving anything under pressure.
