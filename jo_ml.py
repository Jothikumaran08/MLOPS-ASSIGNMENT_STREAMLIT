import streamlit as st
import pickle
import numpy as np

# Load the saved Linear Regression model
with open('pickle.sav', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to convert Gender input to numeric value
def convert_gender_to_numeric(gender):
    if gender.lower() == 'male':
        return 0
    elif gender.lower() == 'female':
        return 1
    else:
        return 2

# Function to convert Occupation input to numeric value
def convert_occupation_to_numeric(occupation):
    occupation_mapping = {
        'Doctor': 0,
        'Engineer': 1,
        'Professor': 2,
        'Student': 3,
        'Teacher': 4
    }
    return occupation_mapping.get(occupation, 5)

# Function to predict Quality_of_Sleep using the loaded model
def predict_Quality_of_Sleep(Gender, Age, Occupation, Stress_Level):
    # Convert Gender and Occupation to numeric
    Gender_numeric = convert_gender_to_numeric(Gender)
    Occupation_numeric = convert_occupation_to_numeric(Occupation)
    
    # Prepare features
    features = np.array([Gender_numeric, Age, Occupation_numeric, Stress_Level])
    features = features.reshape(1, -1)
    
    # Predict Quality_of_Sleep
    Quality_of_Sleep = model.predict(features)
    return Quality_of_Sleep[0]

# Streamlit UI
st.title('Quality_of_Sleep Prediction')
st.write("""
## Input Features
Enter the values for the input features to predict Quality_of_Sleep.
""")

# Input fields for user
Gender = st.text_input('Gender')
Age = st.number_input('Age')
Occupation = st.text_input('Occupation')
Stress_Level = st.number_input('Stress_Level')

# Prediction button
# Prediction button
if st.button('Predict'):
    # Predict Quality_of_Sleep
    Quality_of_Sleep_prediction = predict_Quality_of_Sleep(Gender, Age, Occupation, Stress_Level)
    # Extract the predicted value from the NumPy array
    predicted_hours = Quality_of_Sleep_prediction[0]
    # Format the output
    Quality_of_Sleep_formatted = f"Quality_of_Sleep: {predicted_hours:.2f} Hours"
    st.write(Quality_of_Sleep_formatted)
