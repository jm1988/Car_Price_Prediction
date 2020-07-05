import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import pickle


#loading the model
rf_pkl = open('../models/best_forest.pkl', 'rb')
rf = pickle.load(rf_pkl)


#setting up the trasformations
from encoders import city_enc, make_enc
sc_pkl = open('../models/Fscaler.pkl', 'rb')
scaler = pickle.load(sc_pkl)

def car_preproc(x):
    '''
    x = dictionary with the features as keys
    
    '''
    y = x.copy()
    

    #Encoders
    city_encoder = city_enc
    make_encoder = make_enc 
    
    if y['use'] == 'Personal':
        y['use'] = 1
    else: y['use'] = 0   
    
    y['location'] = city_encoder[y['location']]
    y['name'] = make_encoder[y['name']]   
    
    cols = ['millage', 'location', 'year', 'accidents', 'owners', 'use', 'name']
    
    for k in cols:
        y[k] = (y[k] -  scaler.loc[k,'mean'])/scaler.loc['millage','std']    

#     y['millage'] = (y['millage'] - mill_mu) / mill_sigma
#     y['make'] = (y['make'] - make_mu) / make_sigma

    return y

#Starting the Web App
st.title('Used Cars Price Estimator')
st.write("Please enter the following information to estimate price:")

#millage


name = st.selectbox('Select the Car Name:',
                     list(make_enc.keys()))

year = st.number_input("Enter Car year:", 
                        value = int(),
                        max_value=2020)

millage = st.number_input("Enter Car current Millage:", value = int())


location = st.selectbox('Select City of sale:',
                    list(city_enc.keys()))

accidents = st.number_input('How many accidents the car has had?',
                            value=int())
owners = st.number_input('How many owners the car has had?',
                        value=int())
use = st.selectbox('What has been the main use of this car?',
                    ['Personal','Fleet'])


user_input = {'millage': millage,
             'year': year,
             'name': name,
             'location': location,
             'accidents': accidents,
             'owners': owners,
             'use': use}

#user_input
model_input = car_preproc(user_input)

price = "{:0,.2f}".format(np.round(rf.predict(np.array(list(model_input.values())).reshape(1,-1))[0],2))

st.write("Estimated Car Price = $", price)

#Show progress
#'Starting a long computation...'

    # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

#'...and now we\'re done!'