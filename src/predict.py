import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("models/lap_time_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# Take user input
race = input("Enter Race Name (e.g., Bahrain): ").strip().title()
driver = input("Enter Driver (e.g., VER): ").strip().upper()
lap_number = int(input("Enter Lap Number: "))
stint = int(input("Enter Stint Number: "))
compound = input("Enter Tyre Compound (SOFT/MEDIUM/HARD): ").strip().upper()
tyre_life = int(input("Enter Tyre Life (laps used): "))
position = int(input("Enter Position: "))
team = input("Enter Team: ").strip().title()

# Create input dictionary
sample_input = {
    "RaceName": race,
    "Driver": driver,
    "LapNumber": lap_number,
    "Stint": stint,
    "Compound": compound,
    "TyreLife": tyre_life,
    "Position": position,
    "Team": team
}

# Convert to DataFrame
input_df = pd.DataFrame([sample_input])

# Encode categorical columns
categorical_columns = ["RaceName", "Driver", "Compound", "Team"]

for col in categorical_columns:
    input_df[col] = label_encoders[col].transform(input_df[col])

# Predict
predicted_lap_time = model.predict(input_df)[0]

print("\nPredicted Lap Time:", round(predicted_lap_time, 3), "seconds")