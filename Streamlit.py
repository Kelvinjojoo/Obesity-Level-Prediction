import streamlit as st
import requests

def main():
  st.title('Obesity Level Prediction')
    
  gender= st.radio("Gender", ["Male", "Female"])
  age= st.number_input("Age (years)", min_value=0, max_value=120, value=25)
  height= st.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
  weight= st.number_input("Weight (kilograms)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)
  family_history= st.radio("Family History with Overweight", ["yes", "no"])
  favc= st.radio("Frequent consumption of high caloric food", ["yes", "no"])
  fcvc= st.slider("Frequency of vegetable consumption (1-3)", 1.0, 3.0, 2.0, step=0.1)
  ncp= st.slider("Number of main meals per day", 1.0, 5.0, 3.0, step=0.1)
  caec= st.selectbox("Consumption of food between meals", ["no", "Sometimes", "Frequently", "Always"])
  smoke= st.radio("Do you smoke?", ["yes", "no"])
  ch2o= st.slider("Water consumption (1-3)", 1.0, 3.0, 2.0, step=0.1)
  scc= st.radio("Do you monitor your calorie intake?", ["yes", "no"])
  faf= st.slider("Physical activity frequency (0-3)", 0.0, 3.0, 1.0, step=0.1)
  tue= st.slider("Time using technology devices (0-3)", 0.0, 3.0, 1.0, step=0.1)
  calc= st.selectbox("Consumption of alcohol", ["no", "Sometimes", "Frequently", "Always"])
  mtrans= st.selectbox("Main transportation used", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])
    
  data= {
    'Gender': gender,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'FamilyHistory': family_history,
    'FAVC': favc,
    'FCVC': fcvc,
    'NCP': ncp,
    'CAEC': caec,
    'SMOKE': smoke,
    'CH2O': ch2o,
    'SCC': scc,
    'FAF': faf,
    'TUE': tue,
    'CALC': calc,
    'MTRANS': mtrans
  }

  if st.button('Predict Obesity Level'):
    try:
      response= requests.post('http://127.0.0.1:8000/predict', json= data)
      if response.status_code == 200:
        prediction= response.json()['prediction']
        st.success(f'Predicted Obesity Level: {prediction}')
      else:
        st.error(f'Error {response.status_code}: {response.text}')
    except Exception as e:
        st.error(f'Connection error: {str(e)}')

if __name__ == '__main__':
  main()