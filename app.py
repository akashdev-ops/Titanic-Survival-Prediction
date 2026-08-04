from PIL import Image

image = Image.open("assets/titanic.jpg")

st.image(image, use_container_width=True)
st.markdown("""
<h1 style='text-align:center;
color:#00BFFF;
font-size:50px;'>

🚢 Titanic Survival Prediction

</h1>

<h4 style='text-align:center;color:white;'>

AI Powered Machine Learning Dashboard

</h4>

""", unsafe_allow_html=True)
st.sidebar.image(image,width=250)

st.sidebar.title("Passenger Details")
col1,col2,col3=st.columns(3)

col1.metric(
"🎯 Prediction",
"Survived"
)

col2.metric(
"📊 Accuracy",
"82%"
)

col3.metric(
"⚡ Speed",
"0.01 sec"
)
import plotly.graph_objects as go

fig=go.Figure(go.Indicator(

mode="gauge+number",

value=probability[0][1]*100,

title={"text":"Survival Probability"}

))

st.plotly_chart(fig,use_container_width=True)
fig=go.Figure(

data=[

go.Pie(

labels=["Survive","Not Survive"],

values=[
probability[0][1],
probability[0][0]
]

)

]

)

st.plotly_chart(fig)
tab1,tab2,tab3=st.tabs(

["Prediction","About Model","Dataset"]

)
df=pd.read_csv("Titanic-Dataset.csv")

st.dataframe(df.head())
st.markdown("""

<style>

.stApp{

background:linear-gradient(

135deg,

#0F2027,

#203A43,

#2C5364

);

}

div[data-testid="metric-container"]{

background:rgba(255,255,255,0.15);

padding:20px;

border-radius:20px;

backdrop-filter:blur(15px);

box-shadow:0 8px 32px rgba(0,0,0,.3);

}

</style>

""",unsafe_allow_html=True)
st.markdown("""

---

<center>

Developed by **Akash Dev**

Python • Streamlit • Scikit-Learn

</center>

""",unsafe_allow_html=True)
