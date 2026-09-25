# Microbiological Techniques — Serial Dilution, Spread Plate & Pour Plate

A protocol covering the core quantitative microbiology workflow — serial
dilution followed by spread plating and pour plating — paired with a Python
script that calculates colony-forming units per mL (CFU/mL) from colony
counts, accounting for dilution factor and plating volume.

## Overview

Serial dilution reduces a bacterial suspension to a countable concentration
before plating, since undiluted samples typically produce confluent,
uncountable growth. Spread plating distributes a known volume of diluted
sample across the agar surface using a sterile spreader, producing surface
colonies; pour plating mixes the sample into molten agar before it sets,
producing colonies both on the surface and within the agar. Counting colonies
on a plate within the countable range (typically 30&ndash;300 colonies) and
applying the dilution factor gives the original sample's bacterial
concentration in CFU/mL.

## Principle

- **Serial dilution:** each step reduces concentration by a fixed factor
  (commonly 1:10), so the total dilution after *n* steps is 10⁻ⁿ
- **Spread plate:** known volume spread on agar surface &rarr; surface colonies only
- **Pour plate:** sample mixed into molten agar (~45&deg;C) before pouring &rarr; colonies throughout the agar
- **CFU/mL calculation:** CFU/mL = (colony count &divide; volume plated) &times; dilution factor⁻¹

## Materials & Reagents

- Bacterial culture/sample
- Sterile diluent (saline or phosphate buffer)
- Sterile pipettes/micropipettes and tips
- Sterile Petri dishes and molten nutrient agar (for pour plate)
- Pre-poured nutrient agar plates (for spread plate)
- Sterile glass or plastic spreader (for spread plate)
- Incubator (35&ndash;37&deg;C)
- Colony counter

## Method (Summary)

### Serial Dilution
| Step | Action |
|---|---|
| 1 | Add 1 mL sample to 9 mL diluent (1:10 dilution); mix thoroughly |
| 2 | Transfer 1 mL of that dilution into a fresh 9 mL diluent tube (next 1:10 step) |
| 3 | Repeat to reach the desired dilution range (e.g. 10⁻¹ through 10⁻⁶) |

### Spread Plate
| Step | Action |
|---|---|
| 1 | Pipette a known volume (e.g. 0.1 mL) of a chosen dilution onto agar surface |
| 2 | Spread evenly using a sterile spreader until absorbed |
| 3 | Incubate inverted at 35&ndash;37&deg;C for 18&ndash;24 hours |

### Pour Plate
| Step | Action |
|---|---|
| 1 | Pipette a known volume (e.g. 1 mL) of a chosen dilution into an empty sterile plate |
| 2 | Pour molten agar (cooled to ~45&deg;C) over the sample and swirl gently to mix |
| 3 | Allow to solidify, then incubate inverted at 35&ndash;37&deg;C for 18&ndash;24 hours |

## Result Interpretation

- Only plates with colony counts in the **countable range (30&ndash;300)** should
  be used for CFU/mL calculation — too few colonies gives poor statistical
  reliability, too many risks overlapping/uncountable colonies
- CFU/mL = (colonies counted &divide; volume plated in mL) &times; (1 &divide; dilution factor)

## Analysis Script

`cfu_calculator.py` reads colony counts, plating volume, and dilution factor
for a series of plates from `sample_data/plate_counts.csv`, flags which plates
fall in the countable range, and calculates CFU/mL for each valid plate (and
an average across valid replicates).

### Usage

```bash
pip install -r requirements.txt
python cfu_calculator.py
```

### Sample output

```
Dilution     Volume(mL)   Colonies   Countable?   CFU/mL
---------------------------------------------------------
10^-2        0.1          TNTC       No           —
10^-3        0.1          212        Yes          2.12e+06
10^-4        0.1          34         Yes          3.40e+06
10^-5        0.1          4          No           —

Average CFU/mL (from countable plates): 2.76e+06
```

## Repository Structure

```
microbiological-dilution-plating/
├── README.md
├── cfu_calculator.py
├── requirements.txt
└── sample_data/
    └── plate_counts.csv
```
