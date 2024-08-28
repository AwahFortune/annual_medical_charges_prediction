import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
import sklearn 
  
# loading in the model to predict on the data 
pickle_in = open('model.pkl', 'rb') 
model = pickle.load(pickle_in) 
  
def welcome(): 
    return 'welcome all'
  
# defining the funct sepal_width, petal_length, petal_widthion which will make the prediction using  
# the data which the user inputs 
def prediction(age):   
    prediction = model.predict( 
        [[age]]) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Annual Medical Charge Prediction For Non-Smokers") 
      
    
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    age = st.number_input("Non Smoker Age") 
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = int(prediction(age).item())
    st.success(f'The annual charges of a non-smoker of age {age} is {result}') 
     
if __name__=='__main__': 
    main() 
    