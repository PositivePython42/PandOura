# PandOura v 0.5, based on 30 Days of Streamlit Tutorial but using my own data

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date

st.title('**PandOura** - Data From My Oura Ring')

with st.expander('About this app'):
    st.write('You can use this app to analyse the data from your Oura ring, uploading using the data uplader below.  This product is not authorised by Oura.')
    st.write('If you want to suggest a feature email me at sean@positivepython.co.uk, or raise an issue on GitHub https://github.com/PositivePython42/PandOura/issues')


st.header('Upload your data here')
st.subheader('Please use csv format')
uploaded_file = st.file_uploader("Chose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info('Upload a file')

st.write('What data would you like to see?')
sleep = st.checkbox('Sleep Score')
readiness = st.checkbox('Readiness Score')
steps = st.checkbox('Steps')

if sleep:
    st.write(df['Sleep Score'].describe())
if readiness:
    st.write(df['Readiness Score'].describe())
if steps:
    st.write(df['Steps'].describe())

add_sidebar = st.sidebar.selectbox('Chose Your Dataset', ('Chose', 'Sleep Score', 'Readiness Score', 'Steps'))

if add_sidebar == 'Sleep Score':
    st.write(df['Sleep Score'].describe())
    st.write('You are looking at a summary of ', add_sidebar)
    
if add_sidebar == 'Readiness Score':
    st.write(df['Readiness Score'].describe())
    st.write('You are looking at a summary of ', add_sidebar)
    
if add_sidebar == 'Steps':
    st.write(df['Steps'].describe())
    st.write('You are looking at a summary of ', add_sidebar)


add_sidebar = st.sidebar.selectbox('Chose Your Plot', ('Chose', 'Sleep/Readiness', 'Steps/Sleep'))


if add_sidebar == 'Sleep/Readiness':
    fig = px.scatter(x=df['Sleep Score'], y=df['Readiness Score'])
    st.plotly_chart(fig)
    st.caption('This plot looks at how my sleep score is impacted by the previous days readiness')
    
if add_sidebar == 'Steps/Sleep':
    fig = px.scatter(x=df['Steps'], y=df['Sleep Score'])
    st.plotly_chart(fig)
    st.caption('This plot looks at how my sleep score is impacted by the previous days steps')
    
add_sidebar = st.sidebar.selectbox('Chose Your Linechart', ('Chose', 'Sleep Scores', 'Activity Scores'))

if add_sidebar == 'Sleep Scores':
    chart_data = pd.DataFrame(
        df[['Sleep Score']],
        )
    st.line_chart(chart_data)

if add_sidebar == 'Activity Scores':
    chart_data = pd.DataFrame(
        df[['Activity Score']],
        )
    st.line_chart(chart_data)