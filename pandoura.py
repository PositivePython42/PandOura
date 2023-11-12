#PandOura v 0.6, first version to go on public view as MVP

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def MakeDonut(donut_data):
    #get the percentages, ignore the NaN entries
    red = 0
    amber = 0
    green = 0
    total_count = 0

    for element in df[donut_data]:
        total_count += 1
        if element > 0 and element < 70:
            red += 1
        elif element > 69 and element < 86:
            amber += 1
        elif element > 85:
            green += 1
    red_percent = red / total_count * 100
    amber_percent = amber / total_count * 100
    green_percent = green / total_count * 100

    #Print the donut plot
    donut_show = {'Score Range': ['0 - 69', '70 - 85', '86 - 100'],
                  'Days In Range': [red_percent, amber_percent, green_percent]}
    donut_df = pd.DataFrame(donut_show)
    fig, ax = plt.subplots()
    ax.set_title(donut_data)
    ax.pie(donut_df['Days In Range'], labels=donut_df['Score Range'], labeldistance=1.05,autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors = ['red', 'orange', 'green'])
    centre_circle = plt.Circle((0, 0), 0.80, fc='black')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    plt.show()

st.set_page_config(layout="wide")
st.title('**PandOura** *Open Your Oura* 〇 *Data*')

with st.expander('About this app'):
    st.write('You can use this app to analyse the data from your Oura ring, uploading using the data uplader below.  To download your Oura data;\n'
             '1. Use your browser to go to https://cloud.ouraring.com/trends abd log into your Oura account.\n'
             '2. Chose the data range you want to download. You can do this be selecting the data range on the top graph on this page or using the drop down menu with the dates on it.\n'
             '3. In the top right hand side of the screen press the "Download Data" button\n'
             '4. Chose "Select All" from the drop down menu'
             )
    st.write('Email me at sean@positivepython.co.uk with any feedback, or raise an issues on GitHub https://github.com/PositivePython42/PandOura/issues')

#Upload and perform essential tidy up functions on the data

#Upload the data and replaces blanks with NaN to remove them from skewing analysis
st.header('Upload your data here')
st.subheader('Please use csv format')
uploaded_file = st.file_uploader("Chose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, na_values='')

    # Turn the time/date based data into something Pandas can understand properly
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    #Create a basic dashboard for the 4 main readings Readiness, Sleep, Exercise and Stress
    MakeDonut('Sleep Score')
    MakeDonut('Readiness Score')
    MakeDonut('Activity Score')

else:
    st.info('Upload your Oura Ring data, detailed instructions with screenshots at https://positivepython.co.uk/pandoura/')







"""
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
"""