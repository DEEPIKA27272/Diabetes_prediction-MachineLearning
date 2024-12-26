# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:14:16 2024

@author: deepi
"""

import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model=pickle.load(open('C:/Users/deepi/Downloads/ML STREAMLIT/trained_model.sav','rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    #changing input data into numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshaping the array as we are predicting for one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    #this model tells that we are predicting one data

    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
      return'the person is not diabetic'
    else:
      return'the person is diabetic'
      
def main():
    
    
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #getting input daa from the user
    
    Pregnancies=st.text_input('Number of pregnancies')
    
    Glucose=st.text_input('Glucose Level')
    
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('skin Thickness Value')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction Value')
    Age=st.text_input('Age of the person')
    
    #code for prediction
    diagnosis=''

    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    
    