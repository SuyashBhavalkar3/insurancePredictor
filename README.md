# InsurancePredictor
The Health Insurance Cost Predictor is a machine learning–based web app built with Streamlit that estimates annual insurance premiums based on user inputs like age, sex, BMI, children, and smoking status. It provides personalized predictions, highlights key risk factors, and offers health recommendations for better lifestyle choices. 

---

## ✨ Features
- 🏥 Predict annual health insurance cost using ML model  
- 📊 Input factors: Age, Sex, BMI, Number of children, Smoking status  
- ✅ Risk factor analysis (BMI, smoking, age)  
- 💡 Personalized health recommendations  
- 🎨 Beautiful UI with custom styling and progress indicators  
- 🌐 Ready to deploy on Streamlit Cloud, Render, or other platforms  

---

## 🛠 Tech Stack
- **Frontend & UI**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python  
- **Machine Learning**: scikit-learn  
- **Data Handling**: Pandas, NumPy  
- **Model Persistence**: Pickle  

---

## 📂 Project Structure

insurancePredictor/
│── insuranceCharges.pkl # Trained ML model
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── README.md # Project documentation



---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SuyashBhavalkar3/insurancePredictor.git
   cd insurancePredictor

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the app
streamlit run app.py


