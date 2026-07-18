import streamlit as st
from predict import predict_diabetes

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

# ---------------- Minimal Safe CSS ----------------

st.markdown("""
<style>

.block-container{
    max-width:700px;
    padding-top:2rem;
    padding-bottom:2rem;
}

div.stButton > button{
    width:100%;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------

st.title("🩺 AI Diabetes Prediction System")

st.markdown(
"""
### Early Screening Tool

Predict diabetes risk using Machine Learning.

⚠ **Educational Purpose Only**
"""
)

st.divider()

# ---------------- Sidebar ----------------

st.sidebar.title("📋 About")

st.sidebar.write("""
This application predicts the likelihood of diabetes using a trained Random Forest Machine Learning model.

This prediction is for educational purposes only and should not replace medical advice.
""")

# ---------------- User Inputs ----------------

st.subheader("Enter Patient Information")

preg = st.number_input(
    "Pregnancies",
    min_value=0,
    step=1
)

glucose = st.number_input(
    "Glucose Level",
    min_value=0
)

bp = st.number_input(
    "Blood Pressure",
    min_value=0
)

skin = st.number_input(
    "Skin Thickness",
    min_value=0
)

insulin = st.number_input(
    "Insulin",
    min_value=0
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    format="%.1f"
)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    format="%.3f"
)

age = st.number_input(
    "Age",
    min_value=1
)

st.write("")

# ---------------- Prediction ----------------

if st.button("🩺 Predict Diabetes"):

    prediction, probability = predict_diabetes(
        [
            preg,
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]
    )

    confidence = probability * 100

    st.divider()

    st.subheader("Prediction Result")

    st.progress(float(probability))

    if prediction == 1:

        st.error("⚠ High Risk of Diabetes")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.warning(
            "Please consult a healthcare professional."
        )

    else:

        st.success("✅ Low Risk of Diabetes")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.info(
            "Maintain a healthy lifestyle and regular checkups."
        )

# ---------------- Health Tips ----------------

st.divider()

st.subheader("💡 Health Tips")

tips = [
    "🏃 Exercise for at least 30 minutes daily.",
    "🥗 Eat a balanced diet.",
    "💧 Drink enough water.",
    "🍎 Eat more fruits and vegetables.",
    "🚫 Reduce sugary drinks.",
    "⚖ Maintain a healthy body weight.",
    "🩺 Get regular health checkups."
]

for tip in tips:
    st.write(tip)

# ---------------- Footer ----------------

st.divider()

st.caption(
    "Disclaimer: This application is intended for educational purposes only and should not be used as a medical diagnosis."
)
