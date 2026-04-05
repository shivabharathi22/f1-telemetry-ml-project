import pandas as pd

# Load raw dataset
df = pd.read_csv("data/bahrain_2023_laps.csv")

# Select useful columns
useful_columns = [
    "Driver",
    "DriverNumber",
    "LapNumber",
    "Stint",
    "Compound",
    "TyreLife",
    "LapTime",
    "Position",
    "Team",
    "PitInTime",
    "PitOutTime"
]

# Keep only useful columns
df = df[useful_columns]

# Remove rows where LapTime is missing
df = df.dropna(subset=["LapTime"])

# Remove pit in / pit out laps
df = df[df["PitInTime"].isna()]
df = df[df["PitOutTime"].isna()]

# Convert LapTime to seconds
df["LapTimeSeconds"] = pd.to_timedelta(df["LapTime"]).dt.total_seconds()

# Remove unrealistic lap times
df = df[(df["LapTimeSeconds"] > 80) & (df["LapTimeSeconds"] < 150)]

# Drop pit columns after filtering
df = df.drop(columns=["PitInTime", "PitOutTime"])

# Show first 5 rows
print(df.head())

# Show shape of cleaned dataset
print("\nDataset shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_bahrain_2023_laps.csv", index=False)

print("\nCleaned dataset saved successfully!")