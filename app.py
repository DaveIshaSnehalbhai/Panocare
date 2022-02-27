
import streamlit as st

st.title('Diabeties Prediction System')
s0 = st.number_input('Pregnancies')
s1 = st.number_input('Glucose')
s2 = st.number_input('BloodPressure')  
s3 = st.number_input('SkinThickness')
s4 = st.number_input('BMI')
s6 = st.number_input('DiabetesPedigreeFunction')  
s7 = st.number_input('Age')

from sklearn.datasets import load_diabetes
dia = load_diabetes

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(dia.data,dia.target)

op = model.predict([[s0,s1,s2,s3,s4,s5,s6,s7]])
op = dia.target_number[op[0]]
st.title(op)
    

