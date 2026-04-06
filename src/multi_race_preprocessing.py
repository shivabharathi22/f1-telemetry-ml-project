import pandas as pd

# Load multi-race raw dataset
df = pd.read_csv("data/f1_2023_multi_race_laps.csv")

# Select useful columns
useful_columns = [
    "RaceName",
    "Year",
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
df = df[(df["LapTimeSeconds"] > 60) & (df["LapTimeSeconds"] < 200)]

# Sort properly before creating previous lap feature
df = df.sort_values(["RaceName", "Driver", "LapNumber"])

# Create Previous Lap Time feature
df["PreviousLapTime"] = df.groupby(["RaceName", "Driver"])["LapTimeSeconds"].shift(1)

# Remove rows where previous lap is missing
df = df.dropna(subset=["PreviousLapTime"])

# Drop pit columns after filtering
df = df.drop(columns=["PitInTime", "PitOutTime"])

# Show first 5 rows
print(df.head())

# Show dataset shape
print("\nCleaned multi-race dataset shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_f1_2023_multi_race_laps.csv", index=False)

print("\nCleaned multi-race dataset with PreviousLapTime saved successfully!")