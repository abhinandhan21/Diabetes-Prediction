import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
df = pd.read_csv("Diabetes Predictions.csv")

# Cleaning the data by dropping unnecessary columns and dividing the data into features (X) & target (y)
X = df.drop(columns=['Outcome'])  # Features
y = df['Outcome']  # Target

# Performing train-test split on the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Creating an object for the model for further usage
model = RandomForestClassifier()

# Fitting the model with train data (X_train & y_train)
model.fit(X_train, y_train)

st.header("Diabetes Prediction App")
st.write("Enter the following information to predict whether you might be affected by diabetes.")

# Taking input features from the user
pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0, step=1)
blood_pressure = st.number_input("Blood Pressure", min_value=0, step=1)
skin_thickness = st.number_input("Skin Thickness", min_value=0, step=1)
insulin = st.number_input("Insulin Level", min_value=0, step=1)
bmi = st.number_input("Body Mass Index/BMI", min_value=0, step=0.1)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0, step=0.01)
age = st.number_input("Age", min_value=0, step=1)

# Make a prediction based on the user input
user_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
prediction = model.predict(user_data)[0]

# Display the prediction result
if st.button("Predict"):
    if prediction == 1:
        st.warning("You might be affected by diabetes.")
    elif prediction == 0:
        st.success("You are safe from diabetes.")
