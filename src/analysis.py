import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned_bahrain_2023_laps.csv")

# Group by driver and calculate stats
driver_stats = df.groupby("Driver").agg({
    "LapTimeSeconds": ["mean", "min", "std"]
})

# Rename columns
driver_stats.columns = ["AverageLapTime", "FastestLap", "Consistency"]

# Sort by average lap time
driver_stats = driver_stats.sort_values("AverageLapTime")

# Display results
print("\nDriver Performance:\n")
print(driver_stats)

# -------------------------------
# Graph 1: Average Lap Time
# -------------------------------
plt.figure(figsize=(12, 6))
driver_stats["AverageLapTime"].plot(kind="bar")

plt.title("Average Lap Time by Driver - Bahrain 2023")
plt.xlabel("Driver")
plt.ylabel("Average Lap Time (seconds)")
plt.xticks(rotation=45)

# Zoom in for better visibility
min_time = driver_stats["AverageLapTime"].min()
max_time = driver_stats["AverageLapTime"].max()
plt.ylim(min_time - 0.5, max_time + 0.5)

plt.tight_layout()
plt.savefig("outputs/average_lap_time.png")
print("\nAverage lap time graph saved in outputs folder!")

# -------------------------------
# Graph 2: Driver Consistency
# -------------------------------
plt.figure(figsize=(12, 6))
driver_stats["Consistency"].plot(kind="bar")

plt.title("Driver Consistency (Standard Deviation of Lap Time) - Bahrain 2023")
plt.xlabel("Driver")
plt.ylabel("Consistency (Lower is Better)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/driver_consistency.png")
print("Consistency graph saved in outputs folder!")