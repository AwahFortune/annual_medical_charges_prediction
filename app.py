import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
import requests

st.title("Annual Medical Charge Prediction For Non-Smokers")

# Input features
age = st.number_input("Non Smoker Age")
if st.button("Predict"):
    response = requests.post('http://127.0.0.1:5000/api/predict', json={"age": age})
    result = response.json().get("predictions")
    st.success(f'The annual charges of a non-smoker of age {age} is {result}')


