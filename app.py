import streamlit as st
import pandas as pd
import os


iris_df = pd.read_csv('Iris.csv')

st.image('IrisFlowers.jpg')

st.markdown("<h3 style='text-align: center; color: BLUE;'>Iris Data Statistics</h3>", unsafe_allow_html=True)

stats = iris_df.describe().T

st.dataframe(stats)