import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load cleaned multi-race dataset
df = pd.read_csv("data/cleaned_f1_2023_multi_race_laps.csv")

# Select input features and target
features = [
    "RaceName",
    "Driver",
    "LapNumber",
    "Stint",
    "Compound",
    "TyreLife",
    "Position",
    "Team"
]

target = "LapTimeSeconds"

# Keep only required columns
df = df[features + [target]]

# Remove missing values
df = df.dropna()

# Encode categorical columns
label_encoders = {}
categorical_columns = ["RaceName", "Driver", "Compound", "Team"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split into input (X) and output (y)
X = df[features]
y = df[target]

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model trained successfully!")
print(f"Mean Absolute Error: {mae:.3f} seconds")
print(f"R² Score: {r2:.3f}")

# Save model and encoders
joblib.dump(model, "models/lap_time_model.pkl")
joblib.dump(label_encoders, "models/label_encoders.pkl")

print("\nModel and encoders saved successfully!")