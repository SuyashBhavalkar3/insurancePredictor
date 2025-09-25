import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('insuranceCharges.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
    <style>
    /* Main background */
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #e3f2fd, #f1f8e9);
        color: black;  /* Ensure default text is black */
    }

    /* General card styling */
    .info-box, .metric-card, .status-box {
        border-radius: 0.8rem;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        color: black !important;  /* Force black text */
    }

    /* Info boxes */
    .info-box {
        background: #ffffff;
        border-left: 6px solid #42a5f5;
    }

    /* Make bullet points black */
    .info-box ul, .info-box li {
        color: black !important;
    }

    /* Status colors */
    .status-normal {
        background-color: #d4edda;
        color: #155724 !important;
        border-left: 6px solid #28a745;
    }
    .status-warning {
        background-color: #fff3cd;
        color: #856404 !important;
        border-left: 6px solid #ffc107;
    }
    .status-danger {
        background-color: #f8d7da;
        color: #721c24 !important;
        border-left: 6px solid #dc3545;
    }

    /* Prediction card */
    .metric-card {
        background: linear-gradient(135deg, #42a5f5, #5c6bc0);
        color: black !important;  /* Force black text */
        text-align: center;
        border: none;
    }
    .metric-card h2, .metric-card p {
        color: black !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #42a5f5, #5c6bc0);
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        border-radius: 0.4rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1e88e5, #3949ab);
        transform: translateY(-2px);
    }

    /* BMI Progress bar */
    .bmi-bar {
        height: 20px;
        border-radius: 10px;
        background: #e9ecef;
        overflow: hidden;
        margin: 0.5rem 0 1rem 0;
    }
    .bmi-fill {
        height: 100%;
        border-radius: 10px;
    }
    .bmi-under { background: #ffc107; }
    .bmi-normal { background: #28a745; }
    .bmi-over { background: #ff9800; }
    .bmi-obese { background: #dc3545; }

    /* Headers */
    h1 {
        color: #2c3e50;
        font-weight: 700;
    }
    h2, h3, h4 {
        color: #34495e;
    }

    /* Force all small text and spans to black */
    span, p, li {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏥 Health Insurance Cost Predictor")
st.markdown("""
    This application helps predict your health insurance cost based on various factors.
    Please provide your information below for an estimate.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Information")
    
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    
    sex = st.radio("Sex", ['Male', 'Female'])
    sex_encoded = 1 if sex == 'Female' else 0
    
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    
    smoker = st.radio("Smoking Status", ['Non-smoker', 'Smoker'])
    smoker_encoded = 1 if smoker == 'Smoker' else 0

with col2:
    st.subheader("BMI Information")
    st.markdown("""
    <div class="info-box">
        <h4>BMI Categories:</h4>
        - Underweight: < 18.5<br>
        - Normal weight: 18.5 - 24.9<br>
        - Overweight: 25 - 29.9<br>
        - Obesity: ≥ 30
        <h4>Your BMI Status:</h4>
    </div>
    """, unsafe_allow_html=True)
    
    progress = min(100, int((bmi/40)*100))
    if bmi < 18.5:
        color_class = "bmi-under"
        status_text = "⚠️ You are underweight"
    elif 18.5 <= bmi < 25:
        color_class = "bmi-normal"
        status_text = "✅ You have a normal weight"
    elif 25 <= bmi < 30:
        color_class = "bmi-over"
        status_text = "⚠️ You are overweight"
    else:
        color_class = "bmi-obese"
        status_text = "⚠️ You are in the obese range"

    st.markdown(f"""
        <div class="bmi-bar">
            <div class="bmi-fill {color_class}" style="width:{progress}%"></div>
        </div>
        <div class="status-box {color_class}">
            {status_text}
        </div>
    """, unsafe_allow_html=True)

st.subheader("Health Recommendations")
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    <div class="info-box">
        <h4>Weight Management</h4>
        - Maintain a balanced diet<br>
        - Regular exercise (150 min/week)<br>
        - Stay hydrated<br>
        - Get adequate sleep
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-box">
        <h4>Smoking Cessation</h4>
        - Seek professional help<br>
        - Use nicotine replacement therapy<br>
        - Join support groups<br>
        - Practice stress management
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="info-box">
        <h4>Preventive Care</h4>
        - Regular health check-ups<br>
        - Vaccinations<br>
        - Mental health care<br>
        - Work-life balance
    </div>
    """, unsafe_allow_html=True)

if st.button("Calculate Insurance Cost"):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded]])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader("Estimated Insurance Cost")
    st.markdown(f"""
    <div class='metric-card'>
        <h2>Rs {prediction:,.2f} </h2>
        <p style='color: #f0f0f0; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Estimated Annual Premium</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Risk Factor Analysis")
    
    risk_factors = []
    if bmi >= 25:
        risk_factors.append("High BMI")
    if smoker == 'Smoker':
        risk_factors.append("Smoking")
    if age > 50:
        risk_factors.append("Age")
    
    if risk_factors:
        st.warning("Major factors affecting your insurance cost:")
        for factor in risk_factors:
            st.markdown(f"- {factor}")
    else:
        st.success("You have a relatively low-risk profile!")

st.markdown("""
---
### Additional Resources
- [CDC BMI Calculator](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html)
- [Smoking Cessation Resources](https://www.cdc.gov/tobacco/quit_smoking/index.htm)
- [Healthy Living Guidelines](https://www.who.int/health-topics/healthy-lifestyle)

*Note: This prediction is an estimate based on historical data and should not be considered as the final insurance cost.*
""")
