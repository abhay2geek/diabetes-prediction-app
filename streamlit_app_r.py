import streamlit as st
from predict import predict_diabetes

st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
background:#f5f9fc;
}
.block-container{padding-top:2rem;}
.card{background:white;padding:20px;border-radius:16px;box-shadow:0 4px 15px rgba(0,0,0,.12);}
div.stButton>button{
width:100%;background:#00897b;color:white;border-radius:10px;height:3em;font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 AI Diabetes Prediction System")
st.caption("Early Screening Tool | Educational Purpose Only")
st.caption("Fill in the patient's clinical information.")
st.divider()

c1,c2=st.columns(2)
with c1:
    preg=st.number_input("Pregnancies",0,step=1)
    glucose=st.number_input("Glucose Level",0)
    bp=st.number_input("Blood Pressure",0)
    skin=st.number_input("Skin Thickness",0)
with c2:
    insulin=st.number_input("Insulin",0)
    bmi=st.number_input("BMI",0.0,format="%.1f")
    dpf=st.number_input("Diabetes Pedigree Function",0.0,format="%.3f")
    age=st.number_input("Age",1)

st.sidebar.header("About")
st.sidebar.info("This application predicts diabetes risk using a Machine Learning model.")

if st.button("🩺 Predict Diabetes"):
    prediction, probability=predict_diabetes([preg,glucose,bp,skin,insulin,bmi,dpf,age])
    st.subheader("Prediction Result")
    st.progress(float(probability))
    if prediction==1:
        st.markdown(f"<div class='card'><h3 style='color:#c62828;'>⚠ High Risk of Diabetes</h3><p>Confidence: <b>{probability*100:.2f}%</b></p></div>",unsafe_allow_html=True)
        st.warning("Please consult a healthcare professional.")
    else:
        st.markdown(f"<div class='card'><h3 style='color:#2e7d32;'>✅ Low Diabetes Risk</h3><p>Confidence: <b>{probability*100:.2f}%</b></p></div>",unsafe_allow_html=True)
        st.success("Maintain a healthy lifestyle.")
st.divider()

st.subheader("💡 Health Tips")
st.write("• Exercise at least 30 minutes daily.")
st.write("• Avoid sugary drinks.")
st.write("• Eat fresh fruits and vegetables.")
st.write("• Drink enough water.")
st.write("• Get regular health checkups.")

st.divider()
st.caption(
    "Disclaimer: This tool is for educational purposes only and does not replace professional medical advice."
)
