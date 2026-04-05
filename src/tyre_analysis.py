import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned_bahrain_2023_laps.csv")

# Keep only rows with needed values
df = df.dropna(subset=["Driver", "Stint", "Compound", "TyreLife", "LapTimeSeconds"])

# Sort properly
df = df.sort_values(["Driver", "Stint", "LapNumber"])

# -------------------------------
# Create "lap time delta from stint baseline"
# -------------------------------
# For each Driver + Stint, take the average of the first 2 laps in that stint
# and compare later laps against that baseline.
def add_baseline_delta(group):
    first_laps = group.nsmallest(2, "TyreLife")["LapTimeSeconds"]
    baseline = first_laps.mean()
    group["LapDeltaFromBaseline"] = group["LapTimeSeconds"] - baseline
    return group

df = df.groupby(["Driver", "Stint"], group_keys=False).apply(add_baseline_delta)

# -------------------------------
# Graph 1: Overall relative tyre degradation
# -------------------------------
overall = df.groupby("TyreLife")["LapDeltaFromBaseline"].mean()

plt.figure(figsize=(12, 6))
plt.plot(overall.index, overall.values, marker='o')
plt.title("Relative Tyre Degradation - Bahrain 2023")
plt.xlabel("Tyre Life (Laps on Tyre)")
plt.ylabel("Average Lap Time Increase vs Stint Start (seconds)")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/tyre_degradation_relative.png")
print("Relative tyre degradation graph saved!")

# -------------------------------
# Graph 2: Relative tyre degradation by compound
# -------------------------------
plt.figure(figsize=(12, 6))

for compound in sorted(df["Compound"].dropna().unique()):
    compound_df = df[df["Compound"] == compound]
    compound_avg = compound_df.groupby("TyreLife")["LapDeltaFromBaseline"].mean()
    plt.plot(compound_avg.index, compound_avg.values, marker='o', label=compound)

plt.title("Relative Tyre Degradation by Compound - Bahrain 2023")
plt.xlabel("Tyre Life (Laps on Tyre)")
plt.ylabel("Average Lap Time Increase vs Stint Start (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/tyre_degradation_relative_by_compound.png")
print("Relative tyre degradation by compound graph saved!")

# -------------------------------
# Optional: Single-driver version (more fair)
# -------------------------------
driver_name = "VER"
driver_df = df[df["Driver"] == driver_name]

plt.figure(figsize=(12, 6))

for compound in sorted(driver_df["Compound"].dropna().unique()):
    compound_data = driver_df[driver_df["Compound"] == compound]
    compound_avg = compound_data.groupby("TyreLife")["LapDeltaFromBaseline"].mean()
    plt.plot(compound_avg.index, compound_avg.values, marker='o', label=compound)

plt.title(f"Relative Tyre Degradation by Compound ({driver_name}) - Bahrain 2023")
plt.xlabel("Tyre Life (Laps on Tyre)")
plt.ylabel("Average Lap Time Increase vs Stint Start (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/tyre_degradation_relative_single_driver.png")
print("Single-driver relative tyre graph saved!")