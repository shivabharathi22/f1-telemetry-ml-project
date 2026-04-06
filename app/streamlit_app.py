import streamlit as st
import joblib
import pandas as pd

# Page config
st.set_page_config(page_title="F1 Lap Time Predictor", layout="wide")

# Title
st.title("🏎️ Formula 1 Telemetry and Driver Performance Intelligence System")
st.markdown("Predict lap time and analyze driver performance using Machine Learning.")

# Load model and encoders
model = joblib.load("models/lap_time_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# Dropdown options
race_options = ["Bahrain", "Saudi Arabia", "Australia", "Spain", "Silverstone", "Monza"]
driver_options = ["VER", "PER", "HAM", "RUS", "LEC", "SAI", "ALO", "STR", "NOR", "PIA", "OCO", "GAS", "ALB", "SAR", "BOT", "ZHO", "TSU", "RIC", "MAG", "HUL"]
compound_options = ["SOFT", "MEDIUM", "HARD"]
team_options = [
    "Red Bull Racing", "Mercedes", "Ferrari", "Aston Martin",
    "McLaren", "Alpine", "Williams", "Alfa Romeo",
    "AlphaTauri", "Haas F1 Team"
]

st.markdown("## 🔮 Lap Time Prediction")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    race = st.selectbox("Race Name", race_options)
    driver = st.selectbox("Driver", driver_options)
    lap_number = st.number_input("Lap Number", min_value=1, value=20)
    stint = st.number_input("Stint Number", min_value=1, value=2)

with col2:
    compound = st.selectbox("Tyre Compound", compound_options)
    tyre_life = st.number_input("Tyre Life", min_value=1, value=8)
    position = st.number_input("Position", min_value=1, value=1)
    team = st.selectbox("Team", team_options)

# Predict button
if st.button("Predict Lap Time"):
    input_data = {
        "RaceName": race,
        "Driver": driver,
        "LapNumber": lap_number,
        "Stint": stint,
        "Compound": compound,
        "TyreLife": tyre_life,
        "Position": position,
        "Team": team
    }

    input_df = pd.DataFrame([input_data])

    categorical_columns = ["RaceName", "Driver", "Compound", "Team"]

    try:
        for col in categorical_columns:
            input_df[col] = label_encoders[col].transform(input_df[col])

        prediction = model.predict(input_df)[0]

        st.success(f"🏁 Predicted Lap Time: {round(prediction, 3)} seconds")

    except:
        st.error("Prediction failed. Please check your input values.")

# Divider
st.markdown("---")

# Graph section
st.subheader("📊 Driver Performance Analysis")

st.image("outputs/average_lap_time.png", caption="Average Lap Time by Driver")
st.image("outputs/driver_consistency.png", caption="Driver Consistency Analysis")