# Kolkata House Price Prediction App

A machine learning-powered web app built using Streamlit to predict house prices in Kolkata. The model takes into account the number of bedrooms (BHK), location, total area in square feet, and price per square foot to generate an estimated house price. This tool is designed for potential home buyers, real estate professionals, and data enthusiasts looking to explore real estate trends in Kolkata.

---

## 🌐 Live App 

Check out the live demo here:
🔗 https://kolkata-house-price-prediction-7100.streamlit.app/ 

---

## 🔍 Project Description

This project uses a trained XGBoost Regressor model that analyzes key property features and predicts housing prices accurately. With over 200 locality options, a flexible range of BHK selections from 1 to 20, and a simple interface, this app provides quick and effective results tailored to user input.

---

## ✨ Features

Predict house prices in real-time

Choose from 200+ localities in Kolkata

Select BHK 

Simple, intuitive UI using Streamlit

Accurate predictions powered by XGBoost

Lightweight and runs on local machine

---

## 📊 Model Details

Model: XGBoost Regressor

### Features Used:

BHK

Location (ordinal encoded)

Total Sq. Ft.

Price per Sq. Ft.

### Preprocessing:

Location encoded using OrdinalEncoder

Features scaled using StandardScaler

### Target Variable: Predicted house price in Indian Rupees

---

## 📂 Project Structure

app.py: Main app script

xgb_model.pkl: Pretrained XGBoost model

scaler.pkl: Trained StandardScaler

ordinal_encoder.pkl: Trained encoder for locations

requirements.txt: List of Python packages

README.md: Project description and usage guide

---

## 🚀 Possible Future Enhancements

Add a map for choosing locations visually

Add price trends and market insights with charts

CSV upload for bulk price predictions

Deploy to Streamlit Cloud or Hugging Face

Integrate additional features like floor number, facing, and furnishing type
