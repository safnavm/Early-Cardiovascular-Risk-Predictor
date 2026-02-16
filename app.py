import streamlit as st
import numpy as np
import joblib


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Early Cardiovascular Risk Predictor",
    page_icon="🫀",
    layout="wide"
)
left, center, right = st.columns([2, 6, 2])
with center:
    # entire app content

    # ================= SESSION STATE =================
    if "page" not in st.session_state:
        st.session_state.page = "input"

    # ================= CUSTOM CSS =================
    st.markdown("""
    <style>

    /* ===== BACKGROUND ===== */
    .stApp {
        background: linear-gradient(135deg,   #000428 0%, #004e92 100%);
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
    }
            

    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        color: #ffffff;
        text-align: center;
    }

    /* ===== INPUT LABELS ===== */
    label {
        color: white !important;
        font-weight: 600;
    }

    /* ===== INPUT BOXES ===== */
    input, select {
        background-color: #f8fafc !important;
        color: #020617 !important;
        border-radius: 10px !important;
    }

    /* ===== SECTION TITLE ===== */
    .section-title {
        margin-top: 30px;
        margin-bottom: 10px;
        font-size: 22px;
        font-weight: 700;
        color: #e5e7eb;
        border-bottom: 1px solid rgba(255,255,255,0.3);
        padding-bottom: 5px;
    }


    /* ===== BUTTON CENTER FIX ===== */
    div.stButton > button {
    display: block;
    margin: 0 auto;
    }
            
    .stButton {
        text-align: center;
    }

    .stButton > button {
        background: linear-gradient(135deg, #FFB800, #FFE100);
        color: #1A1A1A;
        border-radius: 14px;
        padding: 14px 70px;
        font-size: 20px;
        font-weight: 1000;
        border: none;
        
        display: inline-block;   /* Important */
        margin: 1000px auto;          /* Centers horizontally */
    }

    /* ===== RESULT TITLES ===== */
    .result-title {
        font-size: 30px;
        font-weight: 800;
        color: #e0f2fe;
        text-align: center;
    }

    .result-subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 15px;
        margin-bottom: 30px;
    }

    .result-section-title {
        font-size: 30px;
        font-weight: 1000;
        color: #bae6fd;
        margin-top: 30px;
        margin-bottom: 14px;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        padding-bottom: 6px;
    }

    .patient-text {
        color: #e5e7eb;
        font-size: 20px;
        line-height: 1.7;
    }

    /* ===== FLOATING ALERT BOXES ===== */
    .alert-box {
        padding: 18px 22px;
        border-radius: 14px;
        margin-top: 14px;
        margin-bottom: 12px;
        font-size: 17px;
        font-weight: 600;
        line-height: 1.6;
        box-shadow: 0 10px 26px rgba(0,0,0,0.15);
        border-left: 8px solid;
    }

    .alert-low {
        background: linear-gradient(135deg, #052e16 , #0a4c28);
        color: #dcfce7;
        border-color: #22c55e;
    }

    .alert-moderate {
        background: linear-gradient(135deg, #422006, #7c4d12);
        color: #ffedd5;
        border-color: #f59e0b;
    }

    .alert-high {
        background: linear-gradient(135deg, #450a0a, #781b1b);
        color: #fee2e2;
        border-color: #ef4444;
    }

    .alert-note {
        font-size: 15px;
        opacity: 0.9;
        margin-top: 6px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= LOAD MODEL =================
    model = joblib.load("cardio_model.pkl")

    
    # ================= INPUT PAGE =========================

    if st.session_state.page == "input":

        st.markdown("<h1>🫀 Early Cardiovascular Risk Predictor</h1>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align:center;font-size:18px;'>Predictive Analytics for Cardiovascular Wellness</p>",
            unsafe_allow_html=True
        )

        st.markdown("<div class='section-title'>👤 Personal Details</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", 18, 100, 40)
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female"])

        # st.markdown("<div class='section-title'>📏 Body Measurements</div>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            height = st.number_input("Height (cm)", 120, 220, 165)
        with col4:
            weight = st.number_input("Weight (kg)", 30, 200, 70)

        st.markdown("<div class='section-title'>🩺 Clinical Indicators</div>", unsafe_allow_html=True)
        col5, col6 = st.columns(2)
        with col5:
            systolic = st.number_input("Systolic BP (mmHg)", 80, 240, 120)
            cholesterol = st.selectbox("Cholesterol Level", ["Normal", "Above Normal", "Well Above Normal"])
        with col6:
            diastolic = st.number_input("Diastolic BP (mmHg)", 50, 160, 80)
            glucose = st.selectbox("Glucose Level", ["Normal", "Above Normal", "Well Above Normal"])

        st.markdown("<div class='section-title'>🏃 Lifestyle Habits</div>", unsafe_allow_html=True)
        col7, col8, col9 = st.columns(3)
        with col7:
            smoker = st.selectbox("Smoking Habit", ["No", "Yes"])
        with col8:
            alcohol = st.selectbox("Alcohol Consumption", ["No", "Yes"])
        with col9:
            active = st.selectbox("Physical Activity", ["No", "Yes"])
        
        col1, col2, col3, = st.columns([2,2,2])
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🔍 Predict Cardiovascular Risk"):
                st.session_state.inputs = {
                    "age": age,
                    "gender": gender,
                    "height": height,
                    "weight": weight,
                    "systolic": systolic,
                    "diastolic": diastolic,
                    "cholesterol": cholesterol,
                    "glucose": glucose,
                    "smoker": smoker,
                    "alcohol": alcohol,
                    "active": active
                }
                st.session_state.page = "result"
                st.rerun()

    
    # ================= RESULT PAGE ========================
left, center, right = st.columns([2, 3, 2])
with center:  
    if st.session_state.page == "result":
      

        data = st.session_state.inputs

        gender = 1 if data["gender"] == "Male" else 0
        cholesterol = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[data["cholesterol"]]
        glucose = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[data["glucose"]]
        smoker = 1 if data["smoker"] == "Yes" else 0
        alcohol = 1 if data["alcohol"] == "Yes" else 0
        active = 1 if data["active"] == "Yes" else 0

        bmi = data["weight"] / ((data["height"] / 100) ** 2)
        age_days = data["age"] * 365

        high_bp = 1 if data["systolic"] > 140 or data["diastolic"] > 90 else 0

        input_data = np.array([[ 
            data["age"], gender, data["height"], data["weight"],
            data["systolic"], data["diastolic"],
            cholesterol, glucose,
            smoker, alcohol, active,
            bmi, high_bp
        ]])

        # input_scaled = scaler.transform(input_data)
        # probability = model.predict_proba(input_scaled)[0][1]
        probability = model.predict_proba(input_data)[0][1]

        risk = round(probability * 100, 2)

        high_risk_flags = 0
        if data["systolic"] >= 160 or data["diastolic"] >= 100:
            high_risk_flags += 1
        if cholesterol == 3:
            high_risk_flags += 1
        if glucose == 3:
            high_risk_flags += 1
        if smoker == 1:
            high_risk_flags += 1
        if bmi >= 30:
            high_risk_flags += 1

        left, center, right = st.columns([1, 2, 1])

        st.markdown("<div class='result-title'>📊 Cardiovascular Risk Assessment Report</div>", unsafe_allow_html=True)
        st.markdown("<div class='result-subtitle'>AI-Driven Cardiovascular Risk Evaluation</div>", unsafe_allow_html=True)

        st.markdown("<div class='result-section-title'>👤 Patient Details</div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="patient-text">
            • <b>Age:</b> {data['age']} years<br>
            • <b>Gender:</b> {data['gender']}<br>
            • <b>Height:</b> {data['height']} cm<br>
            • <b>Weight:</b> {data['weight']} kg
            </div>
            """,
            unsafe_allow_html=True
        )

        # -------- RISK ASSESSMENT --------
        st.markdown("<div class='result-section-title'>📊 Risk Assessment</div>", unsafe_allow_html=True)
        if probability >= 0.75:
            st.markdown(
                f"""
                <div class="alert-box alert-high">
                    <b>High Risk — {risk}%</b>
                    <div class="alert-note">
                        Multiple clinical indicators suggest elevated cardiovascular risk.
                        Medical consultation is strongly recommended.
                    </div>
                </div>
                """, unsafe_allow_html=True)

        elif probability >= 0.5296795062872788:
            st.markdown(
                f"""
                <div class="alert-box alert-moderate">
                    <b>Moderate Risk — {risk}%</b>
                    <div class="alert-note">
                        Some risk factors are present. Lifestyle modification is advised.
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown(
                f"""
                <div class="alert-box alert-low">
                    <b>Low Risk — {risk}%</b>
                    <div class="alert-note">
                        No major risk indicators detected.
                        Maintain the current healthy lifestyle.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
        # st.write("Model Input:", input_data)
        # st.write("Probability:", probability)
    

        # -------- BMI ANALYSIS --------
        st.markdown("<div class='result-section-title'>🧮 BMI Analysis</div>", unsafe_allow_html=True)
        st.markdown(f"<p class='patient-text'><b>BMI Value:</b> {bmi:.2f}</p>", unsafe_allow_html=True)

        if bmi < 18.5:
            st.markdown("""
            <div class="alert-box alert-moderate">
                <b>Underweight</b>
                <div class="alert-note">
                    Nutritional improvement and monitoring are recommended.
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif bmi < 25:
            st.markdown("""
            <div class="alert-box alert-low">
                <b>Normal Body Weight</b>
                <div class="alert-note">
                    BMI is within the healthy range.
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif bmi < 30:
            st.markdown("""
            <div class="alert-box alert-moderate">
                <b>Overweight</b>
                <div class="alert-note">
                    Increased physical activity is recommended.
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="alert-box alert-high">        
                <b>Obese</b>
                <div class="alert-note">
                    High BMI significantly increases cardiovascular risk.
                    Medical advice is strongly recommended.
                </div>
            </div>
            """, unsafe_allow_html=True)

        # -------- KEY RISK CONTRIBUTORS --------
        if probability >= 0.5296795062872788:
            st.markdown("<div class='result-section-title'>🔍 Factors Affecting Your Heart Health</div>", unsafe_allow_html=True)

            contributors = []

            # Blood Pressure
            if data["systolic"] > 140 or data["diastolic"] > 90:
                contributors.append("🔴 Your blood pressure is higher than the healthy range, which can strain the heart.")

            # BMI
            if bmi >= 30:
                contributors.append("🔴 Your body weight is above the recommended range, which may increase heart workload.")
            elif bmi >= 25:
                contributors.append("🟠 Slightly elevated body weight may contribute to cardiovascular stress.")

            # Cholesterol
            if cholesterol == 3:
                contributors.append("🔴 Cholesterol levels are significantly elevated, which may affect blood vessels.")
            elif cholesterol == 2:
                contributors.append("🟠 Cholesterol is slightly above normal.")

            # Glucose
            if glucose == 3:
                contributors.append("🔴 Blood sugar levels are high, which may increase long-term cardiovascular risk.")
            elif glucose == 2:
                contributors.append("🟠 Blood sugar is slightly above normal.")

            # Smoking
            if smoker == 1:
                contributors.append("🔴 Smoking can damage blood vessels and increase heart disease risk.")

            # Physical Activity
            if active == 0:
                contributors.append("🟠 Low physical activity may reduce heart health over time.")

            # Age
            if data["age"] >= 55:
                contributors.append("🟠 Age naturally increases cardiovascular risk over time.")

            # Display results
            if contributors:
                for item in contributors:
                    st.write(item)
            else:
                st.success("✅ No major contributing risk factors were detected based on your inputs.")


        # Recommendations (LOGIC UNCHANGED)
        # st.markdown("<div class='result-section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='result-section-title'>❤️ Personalized Recommendations</div>", unsafe_allow_html=True)

        # ================= PERSONALIZED RECOMMENDATIONS =================
        recommendation_given = False  # Flag to check if any recommendation is printed

        if active == 0:
            st.write("🏃 **Increase physical activity** (at least 30 minutes daily).")
            recommendation_given = True

        if smoker == 1:
            st.write("🚭 **Quit smoking** to reduce cardiovascular risk.")
            recommendation_given = True

        if alcohol == 1:
            st.write("🍷 **Reduce alcohol intake**.")
            recommendation_given = True

        if data["systolic"] > 140 or data["diastolic"] > 90:
            st.write("🩺 **Monitor blood pressure regularly** and consult a doctor.")
            recommendation_given = True

        if cholesterol > 1:
            st.write("🧪 **Manage cholesterol** through diet and medical guidance.")
            recommendation_given = True

        if glucose > 1:
            st.write("🍬 **Monitor blood sugar levels** and maintain a balanced diet.")
            recommendation_given = True

        # If no recommendations were needed
        if not recommendation_given:
            st.write("✅ **Maintain the current healthy lifestyle.**")


        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2, col3, = st.columns([2,2,2])
        with col2:
            if st.button("⬅️ Go Back"):
                st.session_state.page = "input"
                st.rerun()



        st.markdown("</div>", unsafe_allow_html=True)    
        st.markdown(
        """
        <p style='margin-top:20px; font-size:14px; color:#CCCCCC; text-align:center;'>
        ⚠️ This result is generated using a Machine Learning model and is intended for informational purposes only.
        It is not a medical diagnosis. Please consult a qualified healthcare professional for accurate medical advice.
        </p>
        """,
        unsafe_allow_html=True
    )
