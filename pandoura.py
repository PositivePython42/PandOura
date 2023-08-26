# PandOura v 0.4, based on 30 Days of Panda Tutorial up to Day 4, but using my own data

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import date

df = pd.read_csv('/home/seany42/Documents/PandOura/oura_master_data.csv')

st.title('**PandOura** - Data From My Oura Ring')

add_sidebar = st.sidebar.selectbox('Chose Your Dataset', ('Chose', 'Sleep Score', 'Readiness Score', 'Steps'))


if add_sidebar == 'Sleep Score':
    st.write(df['Sleep Score'].describe())
    
if add_sidebar == 'Readiness Score':
    st.write(df['Readiness Score'].describe())
    
if add_sidebar == 'Steps':
    st.write(df['Steps'].describe())

add_sidebar = st.sidebar.selectbox('Chose Your Plot', ('Chose', 'Sleep/Readiness', 'Steps/Sleep'))

st.subheader("Date Range Slider")
date_range = st.slider(
    'Select a date range',
    value=(date(2020, 9, 1), date(2023, 8, 12)))
st.write("Date Range:", date_range)


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