import streamlit as st
import pickle
import numpy as np
import math
import pandas as pd
import joblib

df = pd.read_excel("C:\\Users\\Sariye\\Desktop\\Machine-Learning-Laptops-Price-Prediction\\data_collection\\teknosa_temiz_veri1.xlsx")

# Encoding tablolarını oluştur
marka_mapping = { 6:'HP',
    8:'Lenovo',
    5:'Dell',
    1:'Apple',
    3:'Casper',
    2:'Asus',
    0:'Acer',
    7:'Huwaei',
    9:'MSI',
    4:'DVE'}

islemci_markasi_mapping = {
    2:'Intel',
    0:'AMD',
    1:'Apple'
    }
ekran_karti_mapping = {
    0:'AMD',
    3:'Intel',
    4:'NVIDIA',
    5:'Onboard',
    1:'Apple',
    2:'Diğer'
}

islemci_model_mapping = {
    2:"Core i5",    
    3:"Core i7",    
    10:"Ryzen 7",   
    9:"Ryzen 5" ,   
    1:"Core i3",     
    4:"Core i9",     
    6:"M2",          
    8:"Ryzen 3",     
    5:"M1",           
    0:"Celeron",      
    7:"M2 Pro"                  
}

#modeli yükle
model = joblib.load("C:\\Users\\Sariye\\Desktop\\Machine-Learning-Laptops-Price-Prediction\\algorithms\\gradient_model.pkl")

st.title("LAPTOP FİYAT TAHMİNİ")

#marka
marka = st.selectbox('Marka', df['marka'].map(marka_mapping).unique())

#ssd
ssd = st.selectbox('SSD(GB)',df['SSD(GB)'].unique())

#ekran boyutu
ekran_boyutu =st.selectbox('Ekran Boyutu ',df['ekran_boyutu(inç)'].unique())

#ram
ram = st.selectbox('RAM(GB)',df['RAM(GB)'].unique())

#islemci 
islemci_marka = st.selectbox('İşlemci MarkasI',df['islemci_markasi'].map(islemci_markasi_mapping).unique())
islemci_model = st.selectbox('İşlemci Modeli',df['islemci_modeli'].map(islemci_model_mapping).unique())

#ekran kartı
ekran_karti = st.selectbox('Ekran karti', df['ekran_karti_encoded'].map(ekran_karti_mapping).unique())

if st.button('Fiyatı Tahmin Et'):
    # Kullanıcı girişlerini modele uygun hale getir
    input_data = {
        'marka': [list(marka_mapping.keys())[list(marka_mapping.values()).index(marka)]],
        'SSD(GB)':[ssd],
        'ekran_boyutu(inç)':[ekran_boyutu],
        'RAM(GB)':[ram],
        'islemci_markasi': [list(islemci_markasi_mapping.keys())[list(islemci_markasi_mapping.values()).index(islemci_marka)]],
        'islemci_modeli': [list(islemci_model_mapping.keys())[list(islemci_model_mapping.values()).index(islemci_model)]],
        'ekran_karti_encoded': [list(ekran_karti_mapping.keys())[list(ekran_karti_mapping.values()).index(ekran_karti)]]
    }
    
    input_df = pd.DataFrame(input_data)
    predicted_price = model.predict(input_df)[0]

    st.success(f'Tahmini Fiyat: {predicted_price:.0f} TL')

