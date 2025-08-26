import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('Loan_dataset.sav', 'rb'))

#creating function for prediction
def loan_prediction(input_data):

    #changing input data to numpy arrays
    input_data_as_numpy_array = np.asarray(input_data)

    #Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        st.success("Loan Will Not Be Approved")
    else:
        st.success("Loan Is Approved")
    
    
def main():
    #title for webpage
    st.title('Loan Prediction App')
    
    #getiing input from user
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0
        
    Married = st.selectbox('Married', ['Yes', 'No'])
    if Married == 'Yes':
        Married = 1
    else:
        Married = 0
        
    Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    if Education == 'Graduate':
        Education = 1
    else:
        Education = 0
        
    Self_Employed = st.selectbox('Self-Employed', ['Yes','No'])
    if Self_Employed == 'Yes':
        Self_Employed = 1
    else:
        Self_Employed = 0
        
    ApplicantIncome = st.text_input('ApplicantIncome : ')
    
    CoapplicantIncome = st.text_input('CoapplicantIncome : ')
    
    LoanAmount = st.text_input('LoanAmount : ')
    
    Loan_Amount_Term = st.text_input('Loan_Amount_Term : ')
    
    Credit_History = st.text_input('Credit History: ')
    
    Property_Area = st.selectbox('Property Area', ['Urban', 'Rural', 'SemiUrban' ])
    if Property_Area == 'Urban':
        Property_Area = 1
    elif Property_Area == 'Rural':
        Property_Area = 0
    else:
        Property_Area = 2
    
    #prediction
    report = ''
    
    #button for prediction
    
    if st.button('Loan Prediction Report'):
        report = loan_prediction([Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])
        
    
    
    
if __name__ =='__main__':
    main()