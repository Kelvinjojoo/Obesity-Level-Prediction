from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import joblib
import pandas as pd

app= FastAPI()
model= joblib.load('Obesity.pkl')

class ObesityFeatures(BaseModel):
  Gender: Literal['Male', 'Female']
  Age: int
  Height: float
  Weight: float
  FamilyHistory: Literal['yes', 'no']
  FAVC: Literal['yes', 'no']
  FCVC: float
  NCP: float
  CAEC: Literal['Always', 'Frequently', 'Sometimes', 'no']
  SMOKE: Literal['yes', 'no']
  CH2O: float
  SCC: Literal['yes', 'no']
  FAF: float
  TUE: float
  CALC: Literal['Always', 'Frequently', 'Sometimes', 'no']
  MTRANS: Literal['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking']

@app.get("/")
def read_root():
  return {"message": "Welcome to Obesity Prediction API"}

@app.post('/predict')
def predict(features: ObesityFeatures):
  data= features.dict()
  df= pd.DataFrame([data])
  prediction= model.predict(df)
  return {'prediction': prediction[0]}