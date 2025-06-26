# 🏋🏻 Obesity Level Prediction

This project predicts an individual's obesity level based on lifestyle and physiological attributes using a machine learning model. It includes:

- A trained model (`Obesity.pkl`)
- A REST API built with **FastAPI**
- A user interface built with **Streamlit**

---

## 📁 Project Structure
```
├── Obesity.ipynb # Jupyter Notebook (EDA, training, etc.)
├── Obesity.pkl # Trained Machine Learning model
├── fastAPI.py # FastAPI backend
├── Streamlit.py # Streamlit frontend
└── README.md # Project documentation
```
---

## ⚙️ Setup & Running Instructions

### 🛠️ 1. Create Virtual Environment
```
python -m venv myenv  
.\myenv\Scripts\activate  
pip install --upgrade pip  
pip install pandas numpy matplotlib fastapi pydantic joblib streamlit requests ipykernel scikit-learn xgboost  
python -m ipykernel install --user --name=myenv  
```
---

### 🚀 2. Run FastAPI Backend
```
.\myenv\Scripts\activate  
uvicorn fastAPI:app --reload  
```
- The API will be available at: http://127.0.0.1:8000  
- Swagger UI (interactive docs): http://127.0.0.1:8000/docs  

---

### 🎨 3. Run Streamlit Frontend
```
myenv\Scripts\activate.bat  
streamlit run Streamlit.py  
```
- This will open the Streamlit app in your browser.

---
