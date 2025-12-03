import pandas as pd

# Stage 20 — Data Prep v1
# Loads banks_2008_dataset.csv, validates schema, writes normalized CSV.

INPUT_PATH = "experiments/finance_2008/data/banks_2008_dataset.csv"
OUTPUT_PATH = "experiments/finance_2008/data/banks_2008_dataset_clean.csv"

REQUIRED_COLS = ["bank","quarter","Em","R","Pr","H","G"]

df = pd.read_csv(INPUT_PATH)

# Validate schema
missing = [c for c in REQUIRED_COLS if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

# Sort for determinism
df = df.sort_values(by=["bank","quarter"]).reset_index(drop=True)

# Write cleaned dataset
df.to_csv(OUTPUT_PATH, index=False)

print("Stage 20 Prep OK — wrote:", OUTPUT_PATH)
