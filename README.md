**🔍 Overview**

In the healthcare sector, early diagnosis is crucial for effective treatment. MediGuard AI is a web-based application that leverages Machine Learning algorithms to provide a preliminary assessment of three major diseases based on user input.

The system is designed to be:

Accessible: User-friendly interface for non-technical users.

Fast: Instant predictions using pre-trained models.

Reliable: Built on standard medical datasets (PIMA, Cleveland, Oxford).

**Live Demo / Screenshots**

**Main Dashboard**
<img width="1917" height="919" alt="1) Main Dashboard" src="https://github.com/user-attachments/assets/58794585-058b-4d25-a004-abfe0d1b1584" />
**Diabetes Dashboard**
<img width="1918" height="917" alt="2) Diabetes Default Dashboard" src="https://github.com/user-attachments/assets/0db6436c-7927-4679-a975-f1f602f7fd52" />
**Heart Disease Dashboard**
<img width="1914" height="926" alt="5) Heart Disease Default Dashboard" src="https://github.com/user-attachments/assets/f12c241b-0b25-4239-94d1-987a289053d4" />
**Parkinson's Dashboard**
<img width="1905" height="930" alt="8) Parkinson&#39;s Default Dashboard" src="https://github.com/user-attachments/assets/5e33ea1f-85d4-471e-875a-48c30cc1cf26" />

**🌟 Key Features**

**1. 🍬 Diabetes Prediction**

Algorithm: Support Vector Machine (SVM) / Random Forest

Input: Pregnancies, Glucose, BP, Skin Thickness, Insulin, BMI, Age.

Functionality: Classifies patient as Diabetic or Healthy based on PIMA dataset trends.

**2. ❤️ Heart Disease Prediction**

Algorithm: Logistic Regression

Input: Chest Pain Type, Resting BP, Cholesterol, Max Heart Rate, etc.

Functionality: Assesses cardiac risk factors to predict potential heart disease.

**3. 🧠 Parkinson's Disease Detection**

Algorithm: Support Vector Machine (SVM)

Input: Vocal features (MDVP:Fo, Jitter, Shimmer, Spread1, Spread2).

Functionality: Analyzes voice frequency patterns to detect early signs of Parkinson’s.

**🛠️ Tech Stack**

Frontend,"Streamlit, Streamlit Option Menu"

Backend,Python 3.9+

Machine Learning,"Scikit-Learn, NumPy, Pandas"

Model Saving,Pickle (Joblib)

Development,"VS Code, Jupyter Notebook"

**📊 Model Performance**

We trained and tested our models on standard datasets. Here are the accuracy metrics:

Diabetes Model: 78.2% Accuracy (Random Forest)

Heart Disease Model: 85.1% Accuracy (Logistic Regression)

Parkinson's Model: 87.5% Accuracy (SVM Kernel)

**🚀 Installation Guide**

Follow these steps to run the project locally on your machine.

Prerequisites

Python 3.8 or higher installed.

Step 1: Clone the Repository
git clone https://github.com/YOUR-USERNAME/MediGuard-AI-Multi-Disease-Prediction.git
cd MediGuard-AI-Multi-Disease-Prediction

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Application
streamlit run main.py

**📂 Project Structure**

MediGuard-AI/
├── 📂 data/                # Dataset files (csv)
├── 📂 models/              # Trained models (.sav files)
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   └── scaler.sav
├── main.py                 # Main Streamlit Application
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation

**🔮 Future Scope**

Mobile App: Converting the web app into a mobile application using Flutter/React Native.

Deep Learning: Implementing Neural Networks (ANN/CNN) for higher accuracy.

Report Generation: Auto-generating PDF reports for patients to share with doctors.

More Diseases: Adding modules for Kidney Disease and Liver Disease prediction.

**🤝 Contribution**

Contributions are welcome! If you want to improve the UI or add better models:

Fork the Project.

Create your Feature Branch (git checkout -b feature/NewFeature).

Commit your Changes (git commit -m 'Add some NewFeature').

Push to the Branch (git push origin feature/NewFeature).

Open a Pull Request.

**⚠️ Disclaimer**

This project is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

Made with ❤️ by Md Salman Farsi

Connect with me on 
LinkedIn:https://www.linkedin.com/in/md-salman-farsi-data-analyst | Github:https://github.com/mdsalmanfarsi692004-svg
