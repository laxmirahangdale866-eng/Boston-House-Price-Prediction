import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("Boston_House_Price_Model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Boston House Price Prediction", page_icon="🏠")

st.title("🏠 Boston House Price Prediction")
st.write("Enter the house details below:")

# User Inputs
ID = st.number_input("ID", min_value=1, value=25)
indus = st.number_input("INDUS", value=7.07)
chas = st.selectbox("CHAS (0 = No, 1 = Yes)", [0, 1])
nox = st.number_input("NOX", value=0.469)
rm = st.number_input("RM", value=6.421)
age = st.number_input("AGE", value=78.9)
dis = st.number_input("DIS", value=4.967)
rad = st.number_input("RAD", value=2)
tax = st.number_input("TAX", value=242)
ptratio = st.number_input("PTRATIO", value=17.8)
lstat = st.number_input("LSTAT", value=9.14)

# Predict Button
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "ID": [ID],
        "indus": [indus],
        "chas": [chas],
        "nox": [nox],
        "rm": [rm],
        "age": [age],
        "dis": [dis],
        "rad": [rad],
        "tax": [tax],
        "ptratio": [ptratio],
        "lstat": [lstat]
    })

    prediction = model.predict(input_data)

    st.success(f"🏡 Predicted MEDV: {prediction[0]:.2f}")