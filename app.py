import pandas as pd
import streamlit as st

st.write('# RF ON TIME')
data = pd.read_csv('dash_test1.csv')
st.write('## raw')
data

