import fastf1
import pandas as pd

# Enable cache
fastf1.Cache.enable_cache("cache")

# List of races to load
races = ["Bahrain", "Saudi Arabia", "Australia", "Miami"]

all_laps = []

for race in races:
    print(f"\nLoading {race} 2023 Race data...")
    
    session = fastf1.get_session(2023, race, 'R')
    session.load()

    laps = session.laps.copy()
    laps["RaceName"] = race
    laps["Year"] = 2023

    all_laps.append(laps)

# Combine all races into one dataset
combined_df = pd.concat(all_laps, ignore_index=True)

# Save to CSV
combined_df.to_csv("data/f1_2023_multi_race_laps.csv", index=False)

print("\nMulti-race dataset saved successfully!")
print("Dataset shape:", combined_df.shape)