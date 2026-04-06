# 🏎️ Formula 1 Telemetry and Driver Performance Intelligence System

This project is a Machine Learning and Data Analytics system built using real Formula 1 race data.  
It analyzes driver performance, visualizes lap-time trends, and predicts lap times based on race conditions.

---

## 📌 Project Objective

The goal of this project is to build an intelligent Formula 1 performance analysis system that can:

- Analyze driver race performance
- Compare consistency between drivers
- Study tyre-related race behavior
- Predict lap times using Machine Learning
- Present results through an interactive Streamlit dashboard

---

## 🚀 Features

### ✅ Driver Performance Analysis
- Average lap time by driver
- Fastest lap comparison
- Driver consistency analysis

### ✅ Machine Learning Lap Time Prediction
Predict lap time based on:
- Race Name
- Driver
- Lap Number
- Stint Number
- Tyre Compound
- Tyre Life
- Position
- Team

### ✅ Interactive Dashboard
Built with Streamlit for:
- user input
- lap time prediction
- performance graph visualization

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- FastF1
- Streamlit
- Joblib

---

## 📂 Project Structure

```bash
f1-telemetry-ml-project/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── f1_2023_multi_race_laps.csv
│   └── cleaned_f1_2023_multi_race_laps.csv
│
├── models/
│   ├── lap_time_model.pkl
│   └── label_encoders.pkl
│
├── outputs/
│   ├── average_lap_time.png
│   └── driver_consistency.png
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── tyre_analysis.py
│   ├── multi_race_loader.py
│   ├── multi_race_preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── README.md
├── requirements.txt
└── .gitignore