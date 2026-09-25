"""
cfu_calculator.py

Calculates colony-forming units per mL (CFU/mL) from serial dilution plate
counts, flagging which plates fall within the statistically countable range
(30-300 colonies) and averaging CFU/mL across valid replicates.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "plate_counts.csv"
COUNTABLE_MIN = 30
COUNTABLE_MAX = 300


def load_data(path: Path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def is_countable(colonies_str: str) -> bool:
    if not colonies_str.isdigit():
        return False  # e.g. "TNTC" (too numerous to count)
    count = int(colonies_str)
    return COUNTABLE_MIN <= count <= COUNTABLE_MAX


def calculate_cfu_per_ml(colonies: int, volume_ml: float, dilution_exponent: int) -> float:
    dilution_factor = 10 ** dilution_exponent  # e.g. 10^-3
    return (colonies / volume_ml) / dilution_factor


def main():
    rows = load_data(DATA_PATH)

    print(f"{'Dilution':<13}{'Volume(mL)':<13}{'Colonies':<11}{'Countable?':<13}{'CFU/mL'}")
    print("-" * 62)

    cfu_values = []
    for row in rows:
        exponent = int(row["dilution_exponent"])
        volume = float(row["volume_ml"])
        colonies_str = row["colonies"]
        countable = is_countable(colonies_str)

        if countable:
            cfu = calculate_cfu_per_ml(int(colonies_str), volume, exponent)
            cfu_values.append(cfu)
            cfu_display = f"{cfu:.2e}"
        else:
            cfu_display = "\u2014"

        dilution_label = f"10^{exponent}"
        print(f"{dilution_label:<13}{volume:<13}{colonies_str:<11}{'Yes' if countable else 'No':<13}{cfu_display}")

    if cfu_values:
        avg_cfu = sum(cfu_values) / len(cfu_values)
        print(f"\nAverage CFU/mL (from countable plates): {avg_cfu:.2e}")
    else:
        print("\nNo plates fell within the countable range (30-300 colonies).")


if __name__ == "__main__":
    main()
