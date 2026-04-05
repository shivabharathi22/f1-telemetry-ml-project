import fastf1

# Enable cache so data loads faster after first time
fastf1.Cache.enable_cache('data')

def load_race_data():
    # Load 2023 Bahrain Grand Prix Race
    session = fastf1.get_session(2023, 'Bahrain', 'R')
    session.load()

    laps = session.laps
    return laps

if __name__ == "__main__":
    laps = load_race_data()
    print(laps.head())
    print("\nColumns in dataset:\n")
    print(laps.columns)