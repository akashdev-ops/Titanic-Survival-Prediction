import streamlit as st
import pandas as pd
import joblib
import time

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>

.stApp{
    background-color:#f5f7fa;
}

.main-title{
    font-size:45px;
    font-weight:bold;
    color:#0E76A8;
}

.sub-title{
    font-size:20px;
    color:gray;
}

.card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 0px 15px rgba(0,0,0,.1);
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""",unsafe_allow_html=True)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("Titanic_Model.pkl")

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
"""
<div class="main-title">
🚢 Titanic Survival Prediction
</div>

<div class="sub-title">
AI Powered Machine Learning Dashboard
</div>

<hr>
""",
unsafe_allow_html=True
)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Passenger Details")

pclass=st.sidebar.selectbox("Passenger Class",[1,2,3])

sex=st.sidebar.selectbox(
"Gender",
["Female","Male"]
)

age=st.sidebar.slider(
"Age",
1,
80,
25
)

sibsp=st.sidebar.number_input(
"Siblings/Spouse",
0,
10,
0
)

parch=st.sidebar.number_input(
"Parents/Children",
0,
10,
0
)

fare=st.sidebar.number_input(
"Fare",
0.0,
600.0,
50.0
)

embarked=st.sidebar.selectbox(
"Embarked",
["Cherbourg","Queenstown","Southampton"]
)

predict=st.sidebar.button("🚀 Predict")

# -------------------------------
# Encoding
# -------------------------------
sex=1 if sex=="Male" else 0

embarked={
"Cherbourg":0,
"Queenstown":1,
"Southampton":2
}[embarked]

# -------------------------------
# Prediction
# -------------------------------
if predict:

    start=time.time()

    sample=pd.DataFrame({

"Pclass":[pclass],
"Sex":[sex],
"Age":[age],
"SibSp":[sibsp],
"Parch":[parch],
"Fare":[fare],
"Embarked":[embarked]

})

    prediction=model.predict(sample)

    probability=model.predict_proba(sample)

    end=time.time()

    left,right=st.columns([2,1])

    with left:

        st.subheader("Prediction Result")

        if prediction[0]==1:

            st.success("✅ Passenger is likely to SURVIVE")

            st.balloons()

        else:

            st.error("❌ Passenger is NOT likely to SURVIVE")

        st.subheader("Confidence")

        st.progress(float(probability[0][1]))

        st.write(
        f"### {probability[0][1]*100:.2f}%"
        )

    with right:

        st.subheader("Passenger Summary")

        st.info(f"""

Passenger Class : {pclass}

Gender : {"Male" if sex==1 else "Female"}

Age : {age}

Fare : {fare}

Siblings : {sibsp}

Parents : {parch}

Embarked : {embarked}

""")

    st.divider()

    c1,c2,c3=st.columns(3)

    c1.metric(
        "Model",
        "Logistic Regression"
    )

    c2.metric(
        "Accuracy",
        "82%"
    )

    c3.metric(
        "Prediction Time",
        f"{end-start:.4f} sec"
    )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")

st.markdown(
"""
<div class="footer">

Developed by <b>Akash Dev</b>

Python • Scikit-Learn • Streamlit

</div>
""",
unsafe_allow_html=True
)
