import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
try:
    model = joblib.load("Titanic_Model.pkl")
except:
    st.error("❌ Titanic_Model.pkl not found.")
    st.stop()

# -----------------------------
# Title
# -----------------------------
st.title("🚢 Titanic Survival Prediction")
st.write("Predict whether a passenger would survive the Titanic disaster.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------
pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

sex = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.slider(
    "Age",
    1,
    80,
    25
)

sibsp = st.number_input(
    "Number of Siblings/Spouses",
    0,
    10,
    0
)

parch = st.number_input(
    "Number of Parents/Children",
    0,
    10,
    0
)

fare = st.number_input(
    "Fare",
    0.0,
    600.0,
    32.0
)

embarked = st.selectbox(
    "Embarked",
    ["Cherbourg", "Queenstown", "Southampton"]
)

# -----------------------------
# Encoding
# -----------------------------
sex = 1 if sex == "Male" else 0

embarked_dict = {
    "Cherbourg": 0,
    "Queenstown": 1,
    "Southampton": 2
}

embarked = embarked_dict[embarked]

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    data = pd.DataFrame({
        "Pclass":[pclass],
        "Sex":[sex],
        "Age":[age],
        "SibSp":[sibsp],
        "Parch":[parch],
        "Fare":[fare],
        "Embarked":[embarked]
    })

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("✅ Passenger is likely to SURVIVE")
    else:
        st.error("❌ Passenger is NOT likely to survive")

    st.subheader("Prediction Probability")

    st.progress(float(probability[0][1]))

    st.write(f"**Survival Probability:** {probability[0][1]*100:.2f}%")
    st.write(f"**Death Probability:** {probability[0][0]*100:.2f}%")

st.markdown("---")
st.caption("Developed using Python, Scikit-Learn and Streamlit")