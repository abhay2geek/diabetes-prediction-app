# 🩺 AI Diabetes Prediction System

> An AI-powered web application that predicts the risk of diabetes using Machine Learning and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random_Forest-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📖 Project Overview

The **AI Diabetes Prediction System** is a Machine Learning-based web application that helps estimate the risk of diabetes based on a person's medical information.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**. Users enter their health information through an interactive web interface, and the trained Random Forest model predicts whether they are at a higher or lower risk of diabetes.

> **Note:** This application is intended for educational and awareness purposes only. It is **not** a substitute for professional medical diagnosis.

---

## ✨ Features

- ✅ Diabetes Risk Prediction
- ✅ Machine Learning (Random Forest Classifier)
- ✅ Interactive Streamlit Web Application
- ✅ Prediction Confidence Score
- ✅ Simple & User-Friendly Interface
- ✅ Health Tips and Educational Disclaimer
- ✅ Fast Prediction using Saved Model

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Dataset**

- Pima Indians Diabetes Dataset

**Target Variable**

| Value | Meaning |
|-------:|---------|
| 0 | Non-Diabetic |
| 1 | Diabetic |

---

## 📊 Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── streamlit_app_r.py
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
├── diabetes.csv
├── diabetes_model.pkl
└── scaler.pkl
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/abhay2geek/diabetes-prediction-app.git
```

### Go to the Project Folder

```bash
cd Diabetes-Prediction
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run streamlit_app_r.py
```

The application will open automatically in your browser.

---

## 🔄 Project Workflow

```text
User Input
      │
      ▼
Data Preprocessing
      │
      ▼
Random Forest Model
      │
      ▼
Prediction
      │
      ▼
Risk Assessment
```

---

## 🧪 Sample Input

| Feature | Value |
|---------|------:|
| Pregnancies | 2 |
| Glucose | 120 |
| Blood Pressure | 70 |
| Skin Thickness | 20 |
| Insulin | 85 |
| BMI | 28.5 |
| Diabetes Pedigree Function | 0.35 |
| Age | 35 |

---

## 📈 Sample Output

```text
Prediction

✅ Low Risk of Diabetes

Confidence : 81%
```

---

## 💡 Health Tips

- Exercise for at least 30 minutes daily.
- Eat a balanced diet.
- Reduce sugar intake.
- Drink enough water.
- Get regular health checkups.
- Maintain a healthy body weight.

---

## 🚀 Future Improvements

- PDF Report Generation
- Better User Interface
- Patient History
- Cloud Deployment
- Improved Model Accuracy
- Mobile-Friendly Design

---

## 🌐 Live Demo

🔗 **Try the application here**

https://diabetes-prediction-appgit-zhvqlndx83ptrnhxtptman.streamlit.app

## 👨‍💻 Author

**Abhay Verma**

B.Tech (Artificial Intelligence & Machine Learning)

KIET Group of Institutions

---

## 📄 License

This project is developed for educational purposes only.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
