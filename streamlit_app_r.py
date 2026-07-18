import streamlit as st
from predict import predict_diabetes

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

# -------------------- CSS --------------------

st.markdown("""
<style>

.stApp{
    background:#f4f8fb;
}

.block-container{
    max-width:700px;
    padding-top:2rem;
    padding-bottom:2rem;
}

div.stButton > button{
    width:100%;
    height:3.2em;
    background:#00897B;
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:600;
}

div.stButton > button:hover{
    background:#00695C;
}

.result{
    padding:18px;
    border-radius:12px;
    background:white;
    box-shadow:0px 2px 10px rgba(0,0,0,.15);
}

</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------

st.title("🩺 AI Diabetes Prediction System")

st.markdown(
"""
Early Screening Tool • Educational Purpose Only
"""
)

st.write("Fill in the patient's clinical information below.")

st.divider()

# -------------------- Sidebar --------------------

st.sidebar.title("About")

st.sidebar.info("""
This application predicts diabetes risk using a Random Forest Machine Learning model.

⚠ This is not a medical diagnosis.
""")

# -------------------- Inputs --------------------

preg = st.number_input("Pregnancies", min_value=0, step=1)

glucose = st.number_input("Glucose Level", min_value=0)

bp = st.number_input("Blood Pressure", min_value=0)

skin = st.number_input("Skin Thickness", min_value=0)

insulin = st.number_input("Insulin", min_value=0)

bmi = st.number_input("BMI", min_value=0.0, format="%.1f")

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    format="%.3f"
)

age = st.number_input("Age", min_value=1)

st.write("")

# -------------------- Prediction --------------------

if st.button("🩺 Predict Diabetes"):

    prediction, probability = predict_diabetes(
        [preg, glucose, bp, skin, insulin, bmi, dpf, age]
    )

    confidence = probability * 100

    st.divider()

    st.subheader("Prediction Result")

    st.progress(float(probability))

    if prediction == 1:

        st.error("⚠ High Risk of Diabetes")

        st.markdown(f"""
<div class="result">

<b>Confidence:</b> {confidence:.2f}%<br><br>

Please consult a healthcare professional.

</div>
""", unsafe_allow_html=True)

    else:

        st.success("✅ Low Risk of Diabetes")

        st.markdown(f"""
<div class="result">

<b>Confidence:</b> {confidence:.2f}%<br><br>

Maintain a healthy lifestyle.

</div>
""", unsafe_allow_html=True)

# -------------------- Health Tips --------------------

st.divider()

st.subheader("💡 Health Tips")

tips = [
    "🏃 Exercise at least 30 minutes daily.",
    "🥗 Eat a balanced diet.",
    "💧 Drink enough water.",
    "🚫 Reduce sugary drinks.",
    "⚖ Maintain a healthy weight.",
    "🩺 Get regular health checkups."
]

for tip in tips:
    st.write(tip)

st.divider()

st.caption(
    "Disclaimer: This application is intended for educational purposes only and should not replace professional medical advice."
)
