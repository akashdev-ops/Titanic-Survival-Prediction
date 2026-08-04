import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="wide"
)
st.set_page_config(
    page_title='Titanic Survival Predictor',
    page_icon='🚢',
    layout='wide'
)

# ---------- Sidebar ----------
with st.sidebar:
    st.image('https://cdn-icons-png.flaticon.com/512/3062/3062634.png', width=120)
    st.header('About')

    st.write('**Developer:** Akanksha Pal')
    st.write('**Course:** B.Tech CSE')
    st.write('**Project:** Titanic Survival Prediction')



    st.markdown('---')

    st.info('This project predicts whether a passenger would survive the Titanic disaster based on passenger details.')



import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Page config
st.set_page_config(
    page_title='Titanic Survival Predictor',
    page_icon='🚢',
    layout='wide'
)

# Sidebar here 👇
with st.sidebar:
    st.header('About')
    ...

# Main app starts here 👇
st.markdown('<div class="title">🚢 Titanic Survival Prediction</div>', unsafe_allow_html=True)

# ---------------- Custom CSS ----------------
st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
    }
    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #BBBBBB;
        margin-bottom: 30px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        background-color: #262730;
        color: white;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Header ----------------
st.markdown('<div class="title">🚢 Titanic Survival Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict whether a passenger would survive the Titanic disaster using Machine Learning</div>',
    unsafe_allow_html=True
)

# Titanic image
st.image(
    "https://images.unsplash.com/photo-1518544801976-3e1882f4d4e4?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
)

st.markdown("---")

# ---------------- Training Data ----------------
data = pd.DataFrame({
    'Pclass': [1, 3, 2, 1, 3, 2, 1, 3],
    'Sex':    [0, 1, 0, 1, 1, 0, 0, 1],
    'Age':    [25, 30, 22, 40, 18, 35, 28, 50],
    'SibSp':  [0, 1, 0, 1, 0, 0, 1, 0],
    'Parch':  [0, 0, 0, 1, 0, 0, 1, 0],
    'Fare':   [80, 10, 30, 90, 7, 25, 100, 15],
    'Survived': [1, 0, 1, 1, 0, 1, 1, 0]
})

X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y = data['Survived']

model = LogisticRegression()
model.fit(X, y)

# ---------------- Layout ----------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Passenger Information")

    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.radio("Gender", ["Female", "Male"], horizontal=True)
    age = st.slider("Age", 1, 80, 25)

with col2:
    st.subheader("🎫 Travel Details")

    sibsp = st.number_input("Siblings / Spouses Aboard", 0, 10, 0)
    parch = st.number_input("Parents / Children Aboard", 0, 10, 0)
    fare = st.slider("Fare Paid ($)", 0, 600, 50)

sex_value = 0 if sex == "Female" else 1

st.markdown("")

# ---------------- Prediction ----------------
if st.button("🔍 Predict Survival", use_container_width=True):
    prediction = model.predict([[pclass, sex_value, age, sibsp, parch, fare]])

    if prediction[0] == 1:
        st.balloons()
        st.markdown(
            '<div class="prediction-box">🎉 Passenger is likely to SURVIVE</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="prediction-box">⚠️ Passenger is likely to NOT SURVIVE</div>',
            unsafe_allow_html=True
        )

# ---------------- Footer ----------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        Made with ❤️ by Akash Pratap Dev| B.Tech CSE Student
    </div>
    """,
    unsafe_allow_html=True
)
