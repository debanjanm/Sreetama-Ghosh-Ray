# Clocks and Calendars

> **Difficulty:** Medium  ·  **Target time:** 75 s

## In simple words

**The idea:** A clock's hands move at fixed speeds, and the days of the week repeat every 7 days.

**Think of it like:** The minute hand is a fast runner (6° per minute), the hour hand a slow walker (0.5° per minute).

**Simple steps:**
1. Hour hand angle = 30 × hours + 0.5 × minutes.
2. Minute hand angle = 6 × minutes.
3. Subtract. If the result is over 180°, use 360° minus it for the smaller angle.
4. Calendars: divide days by 7; the remainder is how many weekdays to move forward.

**Watch out:** Always give the smaller angle unless the question asks otherwise.

## Formulas
Minute hand: 6° per minute. Hour hand: 0.5° per minute, starting 30° per hour from 12. Raw angle=|30H−5.5M|; smaller angle=min(raw,360−raw).

## Recognise and solve
1. At 3:20, hour hand=90+10=100°, minute=120°; smaller angle **20°**.
2. At 9:00, raw difference 270°; smaller angle 360−270=**90°**.
3. If today is Tuesday, 10 days later is 10 mod 7=3 days later → **Friday**.

## Tips and traps
The hour hand moves between hour marks. For calendar date questions, distinguish “after 10 days” from inclusive counting; leap-year rules: divisible by 4 except century years unless divisible by 400.

## Try it
Angle at 2:30? **Answer:** minute 180°, hour 75°, smaller angle 105°.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: What is the smaller angle between clock hands at 3:30?

**Solution:** Minute hand=180°; hour hand=3×30°+30×0.5°=105°. Difference=**75°**.

### Pattern 2: If 1 January is a Monday in a non-leap year, what day is 1 February?

**Solution:** January has 31 days, shifting by 31 mod 7=3 days. Monday+3=**Thursday**.

### Pattern 3: How many odd days are there in a leap year?

**Solution:** 366 mod 7=**2 odd days**; an ordinary year has 1.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- The hands overlap every 65 5/11 minutes. In 12 hours they overlap 11 times, are opposite 11 times and are at right angles 22 times; in 24 hours, double each.
- Hands overlap between H and H+1 at 60H/11 minutes past H.
- A clock that gains or loses x minutes per hour shows an error of x × (hours passed) after that time.
- Odd days: an ordinary year has 1, a leap year has 2. 100 years = 5 odd days, 200 = 3, 300 = 1, 400 = 0.
- Reference: 1 January 2001 was a Monday.

### Medium patterns

**M1. Smaller angle between the hands at 7:20?**

**Solution:** Hour hand = 210+10 = 220°; minute hand = 120°; difference **100°**.

**M2. 15 August 2025 is Friday. What day is 15 August 2026?**

**Solution:** 365 days = 52 weeks + 1 day, so **Saturday**.

### Hard patterns

**H1. At what time between 4 and 5 are the hands together?**

**Solution:** 60×4/11 = 21 9/11 minutes, so about **4:21:49**.

**H2. A clock gains 2 minutes every hour and is set right at noon on Monday. What does it show at real noon on Tuesday?**

**Solution:** Gain = 24×2 = 48 minutes, so it shows **12:48 pm**.

### Practice (answers hidden)
1. Angle between the hands at 6:00?
2. 1 January 2001 is Monday. What day is 1 January 2002?
3. How many odd days are there in 100 years?

<details><summary>Answers</summary>

1. **180°**.
2. 365 days gives 1 odd day: **Tuesday**.
3. **5**.

</details>
