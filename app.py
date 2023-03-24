import pandas as pd
import streamlit as st
import numpy as np
import pickle
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


st.set_page_config(layout='wide')
cleaned_data = pd.read_csv('cleaned_data.csv')


def change(obj):
    obj = obj.replace(',', '')
    return obj


def change1(obj):
    temp = 0
    if (obj.isnumeric() == True) & (obj != '0'):
        temp = obj
    return temp


def change2(obj):
    s = ''
    t = obj.split()[0:3]
    for i in t:
        s = s + ' ' + i
    return s


def empty_space():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write('')
        st.write('')
        st.write('')
    with col5:
        pass
    with col6:
        pass


companies_drop_down = cleaned_data['Company'].unique()
model_drop_down = cleaned_data['Car_Name'].unique()
year_drop_down = cleaned_data['Year'].unique()
kms_drop_down = cleaned_data['Kms_Driven'].unique()
fuel_drop_down = cleaned_data['Fuel_Type'].unique()

st.title('Car Price Prediction Model')

col1, col2, col3 = st.columns(3)
with col1:
    companies = st.selectbox('Select Company', companies_drop_down)
with col2:
    model = st.selectbox('Select Model', model_drop_down)
with col3:
    year = st.selectbox('Select Purchase Year', year_drop_down)

col4, col5 = st.columns(2)
with col1:
    fuel = st.selectbox('Select Fuel Type', fuel_drop_down)
with col2:
    kms = st.selectbox('Select Kms Travelled', kms_drop_down)

empty_space()

pipe = pickle.load(open('Model.pkl', 'rb'))

btn = st.button(label='Predict Price')

empty_space()

if btn:
    prediction = pipe.predict(pd.DataFrame(np.array([model, companies, year, kms, fuel]).reshape(1, 5), columns=['Car_Name', 'Company', 'Year', 'Kms_Driven', 'Fuel_Type']))
    col1, col2, col3, col4, clo5 = st.columns(5)
    with col1:
        st.subheader('Predicted Price is : ')
    with col2:
        x = str(prediction[0])[0:9]
        st.subheader(x + ' rupees')
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
