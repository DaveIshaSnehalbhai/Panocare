
import streamlit as st

st.title('Diabeties Prediction System')
s0 = st.slider('Pregnancies',0,10,1)
s1 = st.slider('Glucose',0,200,1)
s2 = st.slider('BloodPressure',0,120,1)
s3 = st.slider('SkinThickness',0,100,1)
s4 = st.slider('BMI'0,50,0.1)
s5=st.slider('Insulin',0,1000,1)
s6 = st.slider('DiabetesPedigreeFunction',0,2,0.01)
s7 = st.slider('Age',1,100,1)

from sklearn.datasets import load_diabetes
dia = load_diabetes

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(dia.x,dia.y)

op = model.predict([[s0,s1,s2,s3,s4,s5,s6,s7]])
op = dia.y[op[0]]
st.title(op)
    

