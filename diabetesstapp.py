import streamlit as st
import requests
import os
import json

API_URLBASE = os.getenv("API_URLBASE")
API_KEY = os.getenv("API_KEY")

def execute_prediction_request(pregnancies: int, glucose: float, blood_pressure: float, skin_thickness: float,
                                insulin: float, bmi: float, diabetes_pedigree_function: float, age: int) -> bool:

    payload = {
        'pregnancies': pregnancies,
        'glucose': glucose,
        'blood_pressure': blood_pressure,
        'skin_thickness': skin_thickness,
        'insulin': insulin,
        'bmi': bmi,
        'diabetes_pedigree_function': diabetes_pedigree_function,
        'age': age
    }
    
    headers_dict = {'x-api-key': API_KEY}
    
    response = requests.post(API_URLBASE + '/diabetes-predictions', headers=headers_dict, data=json.dumps(payload))
    
    if response.status_code == 201:       
        return response.json().get('has_diabetes')
    else:
        response.raise_for_status()


header_container = st.container()

with header_container:
    st.title('Diabetes Prediction Form')
    st.write('Fill in the following form to check for a possible case of Diabetes')
    

with st.form(key='diabetes-pred-form'):
    col1, col2 = st.columns(2)
    
    pregnancies = col1.slider(label='Number of Pregnancies:', min_value=0, max_value=15)
    glucose = col1.text_input(label='Glucose:')
    blood_pressure = col1.text_input(label='Blood Pressure:')
    skin_thickness = col1.text_input(label='Skin Thickness:')
    insulin = col2.text_input(label='Insulin:')
    bmi = col2.text_input(label='Body Mass Index (BMI):')
    diabetes_pedigree = col2.text_input(label='Diabetes Pedigree Function:')
    age = col2.slider(label='Age:', min_value=1, max_value=120)
    
    submit = st.form_submit_button(label='Check')
    
    if submit:
        try:
            has_diabetes = execute_prediction_request(pregnancies, glucose, blood_pressure, skin_thickness,
                                                      insulin, bmi, diabetes_pedigree, age)
            
            if has_diabetes:
                st.error('The entered data suggests a POSITIVE case of Diabetes!')
            else:
                st.success('The entered data suggests a NEGATIVE case of Diabetes!')
                
        except requests.exceptions.RequestException as ex:
            st.error('Oops!! Something went wrong in communicating with the prediction service.')
