import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
import os

st.set_page_config(
    page_title="MediGuard AI | Multi-Disease Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        text-align: center;
    }
    
    .sky-box {
        background-color: #4FC3F7;  
        color: #000000;             
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #0288D1;  
        margin-bottom: 10px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    .yellow-box {
        background-color: #FBC02D;  
        color: #000000;             
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #F57F17;  
        margin-bottom: 10px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    div.stButton > button {
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        height: 60px;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 6px 10px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

def load_model(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "SAVED_MODELS", filename)
    if os.path.exists(path):
        return pickle.load(open(path, 'rb'))
    return None

diabetes_model = load_model('diabetes_model.sav')
heart_model = load_model('heart_disease_model.sav')
parkinsons_model = load_model('parkinsons_model.sav')
scaler = load_model('scaler.sav')

with st.sidebar:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=120)

    st.markdown("<h1 style='text-align: center; margin-top: -10px;'>MediGuard AI</h1>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None, 
        options=["Home", "Diabetes", "Heart Disease", "Parkinson's Disease"],
        icons=["house", "droplet", "heart", "activity"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2E86C1"},
        }
    )
    st.markdown("---")
    
    warning_icon_url = "https://cdn-icons-png.flaticon.com/512/12104/12104722.png" 

    if selected == "Diabetes":
        c1, c2, c3 = st.columns([1, 2, 1]) 
        with c2:
            st.image("https://img.icons8.com/color/480/syringe-with-a-drop-of-blood.png", width=100)
        
        st.markdown(f"""
            <div class="sky-box">
                ℹ️ Instructions<br>
                <span style="font-weight: normal;">Input Patient Metrics To Generate A Health Report.</span>
            </div>
            <div class="yellow-box">
                <img src="{warning_icon_url}" width="20" style="vertical-align: middle;"/> Disclaimer<br>
                <span style="font-weight: normal;">Consult An Endocrinologist For Medical Advice.</span>
            </div>
            """, unsafe_allow_html=True)
        
    elif selected == "Heart Disease":
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image("https://cdn-icons-png.flaticon.com/512/2966/2966486.png", width=100)
            
        st.markdown(f"""
            <div class="sky-box">
                ℹ️ Instructions<br>
                <span style="font-weight: normal;">Enter Clinical Vitals For Cardiac Assessment.</span>
            </div>
            <div class="yellow-box">
                <img src="{warning_icon_url}" width="20" style="vertical-align: middle;"/> Disclaimer<br>
                <span style="font-weight: normal;">Always Consult A Cardiologist For Medical Advice.</span>
            </div>
            """, unsafe_allow_html=True)
        
    elif selected == "Parkinson's Disease":
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image("https://cdn-icons-png.flaticon.com/512/2491/2491325.png", width=100)

        st.markdown(f"""
            <div class="sky-box">
                ℹ️ Instructions<br>
                <span style="font-weight: normal;">Input Vocal Resonance Metrics.</span>
            </div>
            <div class="yellow-box">
                <img src="{warning_icon_url}" width="20" style="vertical-align: middle;"/> Disclaimer<br>
                <span style="font-weight: normal;">Always Consult A Neurologist For Medical Advice.</span>
            </div>
            """, unsafe_allow_html=True)

if selected == "Home":
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏥 MediGuard AI System</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #888;'>Advanced Multi-Disease Prediction Platform</h3>", unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background-color: rgba(46, 134, 193, 0.15); 
            padding: 16px; 
            border-radius: 0.5rem; 
            border: 1px solid #2E86C1; 
            color: #ffffff;
            margin-bottom: 10px;">
            <h3 style="margin: 0; color: #4FC3F7; font-size: 20px; font-weight: bold;">🩸 Diabetes</h3>
            <p style="margin: 0; font-size: 16px; margin-top: 5px;">Analyze Glucose And BMI To Assess Diabetic Risks.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background-color: rgba(192, 57, 43, 0.15); 
            padding: 16px; 
            border-radius: 0.5rem; 
            border: 1px solid #C0392B; 
            color: #ffffff;
            margin-bottom: 10px;">
            <h3 style="margin: 0; color: #E74C3C; font-size: 20px; font-weight: bold;">❤️ Heart Disease</h3>
            <p style="margin: 0; font-size: 16px; margin-top: 5px;">Evaluate Cardiovascular Health Via Clinical Vitals.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background-color: rgba(142, 68, 173, 0.15); 
            padding: 16px; 
            border-radius: 0.5rem; 
            border: 1px solid #8E44AD; 
            color: #ffffff;
            margin-bottom: 10px;">
            <h3 style="margin: 0; color: #A569BD; font-size: 20px; font-weight: bold;">🧠 Parkinson's</h3>
            <p style="margin: 0; font-size: 16px; margin-top: 5px;">Detect Neurological Patterns In Vocal Resonance.</p>
        </div>
        """, unsafe_allow_html=True)

if selected == "Diabetes":
    st.markdown("""<style>div.stButton > button {background: linear-gradient(90deg, #2E86C1 0%, #4FC3F7 100%);}</style>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩸 Diabetes Disease Prediction 🩸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>AI-Powered Diabetes Risk Analysis.</p>", unsafe_allow_html=True)
    st.divider()

    if not diabetes_model:
        st.error("⚠️ Error: 'diabetes_model.sav' not found in SAVED_MODELS.")
    else:
        st.subheader("📝 Patient Information")
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, key='d1')
            Glucose = st.number_input('Glucose Level', min_value=0, key='d2')
            BloodPressure = st.number_input('Blood Pressure', min_value=0, key='d3')
            SkinThickness = st.number_input('Skin Thickness', min_value=0, key='d4')
        with col2:
            Insulin = st.number_input('Insulin Level', min_value=0, key='d5')
            BMI = st.number_input('BMI', min_value=0.0, format="%.1f", key='d6')
            DPF = st.number_input('Diabetes Pedigree Function', min_value=0.000, format="%.3f", key='d7')
            Age = st.number_input('Age', min_value=0, step=1, key='d8')

        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            analyze = st.button('🔍 Analyze Diabetes Risk', use_container_width=True)

        if analyze:
            input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]])
            prediction = diabetes_model.predict(input_data)
            
            st.markdown("---")
            if prediction[0] == 1 or str(prediction[0]) == '1':
                st.error("⚠️ **Result: POSITIVE (Diabetic Indicators Found)**")
                with st.expander("💊 Recommended Next Steps (Click to Open)"):
                    st.markdown("""
                    1. **Consultation:** Visit An Endocrinologist Immediately.
                    2. **Testing:** A Clinical **HbA1c Test** Is Recommended.
                    3. **Diet:** Reduce Refined Sugars And Processed Foods.
                    4. **Activity:** Incorporate 30 Mins Of Daily Walking.
                    """)
            else:
                st.success("✅ **Result: NEGATIVE (Not Diabetic)**")
                with st.expander("🥗 Preventive Health Tips (Click To Open)"):
                    st.markdown("""
                    * **Hydration:** Drink 3-4 Liters Of Water Daily.
                    * **Diet:** Eat Fiber-Rich Foods (Vegetables, Whole Grains).
                    * **Checkups:** Yearly Blood Sugar Tests Are Good Practice.
                    """)

if selected == "Heart Disease":
    st.markdown("""<style>div.stButton > button {background: linear-gradient(90deg, #C0392B 0%, #E74C3C 100%);}</style>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #C0392B;'>❤️ Heart Disease Prediction ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>AI-Powered CardioVascular Risk Assessment.</p>", unsafe_allow_html=True)
    st.divider()

    if not heart_model:
        st.error("⚠️ Error: 'heart_disease_model.sav' not found in SAVED_MODELS.")
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=1, key='h1')
            sex = st.selectbox('Sex', ['Male', 'Female'], key='h2')
            sex_val = 1 if sex == 'Male' else 0
            cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], key='h3')
        with col2:
            trestbps = st.number_input('Resting BP', min_value=50, key='h4')
            chol = st.number_input('Cholesterol', min_value=100, key='h5')
            fbs = st.selectbox('Fasting Blood Sugar > 120', [0, 1], key='h6')
            restecg = st.selectbox('Resting ECG', [0, 1, 2], key='h7')
        with col3:
            thalach = st.number_input('Max Heart Rate', min_value=60, key='h8')
            exang = st.selectbox('Exercise Angina', [0, 1], key='h9')
            oldpeak = st.number_input('Oldpeak', min_value=0.0, format="%.1f", key='h10')
            slope = st.selectbox('Slope', [0, 1, 2], key='h11')
            ca = st.selectbox('Major Vessels (0-3)', [0, 1, 2, 3], key='h12')
            thal = st.selectbox('Thal', [1, 2, 3], key='h13')

        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            analyze = st.button('🫀 Analyze Heart Risk', use_container_width=True)

        if analyze:
            input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = heart_model.predict(input_data)
            
            st.markdown("---")
            if prediction[0] == 1 or str(prediction[0]) == '1':
                st.error("⚠️ **Result: POSITIVE (Heart Disease Detected)**")
                with st.expander("🚑 Emergency & Medical Recommendations"):
                    st.markdown("""
                    1. **Consultation:** Book An Appointment With A Cardiologist.
                    2. **Tests:** You May Need An Angiogram Or Stress Test.
                    3. **Diet:** Avoid Trans Fats, High Sodium, And Red Meat.
                    4. **Warning Signs:** If You Feel Chest Pain, Call Emergency Services.
                    """)
            else:
                st.success("✅ **Result: NEGATIVE (Healthy Heart)**")
                with st.expander("❤️ Maintenance Tips"):
                    st.markdown("""
                    * **Diet:** Eat Fruits, Vegetables, And Whole Grains.
                    * **Exercise:** Aim For 150 Minutes Of Moderate Cardio Per Week.
                    * **Habits:** Avoid Smoking And Limit Alcohol Intake.
                    """)

if selected == "Parkinson's Disease":
    st.markdown("""<style>div.stButton > button {background: linear-gradient(90deg, #8E44AD 0%, #A569BD 100%);}</style>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #8E44AD;'>🧠 Parkinson's Disease Prediction 🧠</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Neurological Pattern Detection Via Vocal Metrics.</p>", unsafe_allow_html=True)
    st.divider()

    if not parkinsons_model or not scaler:
        st.error("⚠️ Error: Model or Scaler not found in SAVED_MODELS.")
    else:
        st.subheader("📋 Vocal Resonance Metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            fo = st.number_input('MDVP:Fo(Hz)', value=119.99, key='p1')
            fhi = st.number_input('MDVP:Fhi(Hz)', value=157.30, key='p2')
            flo = st.number_input('MDVP:Flo(Hz)', value=74.99, key='p3')
            jit_per = st.number_input('MDVP:Jitter(%)', format="%.5f", key='p4')
            jit_abs = st.number_input('MDVP:Jitter(Abs)', format="%.5f", key='p5')
            rap = st.number_input('MDVP:RAP', format="%.5f", key='p6')
            ppq = st.number_input('MDVP:PPQ', format="%.5f", key='p7')
            ddp = st.number_input('Jitter:DDP', format="%.5f", key='p8')
        with col2:
            shimmer = st.number_input('MDVP:Shimmer', format="%.5f", key='p9')
            shimmer_db = st.number_input('MDVP:Shimmer(dB)', format="%.5f", key='p10')
            apq3 = st.number_input('Shimmer:APQ3', format="%.5f", key='p11')
            apq5 = st.number_input('Shimmer:APQ5', format="%.5f", key='p12')
            apq = st.number_input('MDVP:APQ', format="%.5f", key='p13')
            dda = st.number_input('Shimmer:DDA', format="%.5f", key='p14')
            nhr = st.number_input('NHR', format="%.5f", key='p15')
            hnr = st.number_input('HNR', format="%.5f", key='p16')
        with col3:
            rpde = st.number_input('RPDE', format="%.5f", key='p17')
            dfa = st.number_input('DFA', format="%.5f", key='p18')
            spread1 = st.number_input('spread1', format="%.5f", key='p19')
            spread2 = st.number_input('spread2', format="%.5f", key='p20')
            d2 = st.number_input('D2', format="%.5f", key='p21')
            ppe = st.number_input('PPE', format="%.5f", key='p22')

        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            analyze = st.button("🧠 Analyze Status", use_container_width=True)

        if analyze:
            input_data = np.array([[fo, fhi, flo, jit_per, jit_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
            std_data = scaler.transform(input_data)
            prediction = parkinsons_model.predict(std_data)
            
            st.markdown("---")
            if prediction[0] == 1 or str(prediction[0]) == '1':
                st.error("⚠️ **Result: POSITIVE (Parkinson's Detected)**")
                with st.expander("🚑 Recommended Next Steps"):
                    st.markdown("""
                    1. **Consultation:** Visit A Neurologist For Clinical Evaluation.
                    2. **Therapy:** Speech Therapy And Physical Therapy Can Help.
                    3. **Medication:** Discuss Dopamine-Supportive Medications With Your Doctor.
                    """)
            else:
                st.success("✅ **Result: NEGATIVE (Healthy)**")
                with st.expander("🧠 Brain Health Tips"):
                    st.markdown("""
                    * **Exercise:** Regular Aerobic Exercise Protects The Brain.
                    * **Diet:** Eat Antioxidants (Berries, Nuts) And Omega-3s.
                    * **Sleep:** Ensure 7-8 Hours Of Quality Sleep Daily.
                    """)