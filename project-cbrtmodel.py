import streamlit as st
import pandas as pd
from pickle import load
import numpy as np



st.title('Combined Cycle Power Plant')
st.subheader('Regression Model To Predict The Energy Generated')


def page():
    
    temp=st.sidebar.number_input('Temperature(°C)')    
    exha=st.sidebar.number_input('Exhaust Vacuum(cmHg)')
    amb=st.sidebar.number_input('Ambient Pressure(millibar)')
    hum=st.sidebar.number_input('Relative Humidity(%)')
    
    
    data_dict= {'temperature':temp,'exhaust_vacuum':exha,'amb_pressure':amb,'r_humidity':hum }
    df=pd.DataFrame(data_dict,index=[1])
    df_new=np.cbrt(df)
    return df_new

features=page()
if st.sidebar.button('Submit'):
    st.write(features**3)
    loaded_model= load(open('cubrt_model.pkl','rb'))
    result=loaded_model.predict(features)
    result_1=result**3
    result_2=result_1[0]
    formatted_number = "{:.2f}".format(result_2)
    st.write( f'Energy Generated : {formatted_number} MW')
    

