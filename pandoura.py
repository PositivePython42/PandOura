# PandOura v 0.6, first version to go on public view as MVP

import pandas as pd
import streamlit as st


st.set_page_config(layout="wide")
st.title('**PandOura** - Data From My Oura Ring')

with st.expander('About this app'):
    st.write('You can use this app to analyse the data from your Oura ring, uploading using the data uplader below.  To download your Oura data;\n'
             '1. Use your browser to go to https://cloud.ouraring.com/trends\n'
             '2. Chose the data range you want to download. You can do this be selecting the data range on the top graph on this page or using the drop down menu with the dates on it\n'
             '3. In the top right hand side of the screen press the "Download Data" button\n'
             '4. Chose "Select All" from the drop down menu'
             )
    st.write('Please suggest a feature.  Email me at sean@positivepython.co.uk, or raise an issue on GitHub https://github.com/PositivePython42/PandOura/issues')

#Upload and perform essential tidy up functions on the data
#Upload the data
st.header('Upload your data here')
st.subheader('Please use csv format')
uploaded_file = st.file_uploader("Chose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info('Upload a file')

#Turn the time/date based data into something Pandas can understand properly
df['date'] = pd.to_datetime(df['date'], dayfirst=True)


#Replace all the blank data items with a code Pandas uses to exclude the date, otherwise it skews the analysis#



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