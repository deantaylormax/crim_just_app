import streamlit as st
import pandas as pd 
import numpy as np 
import altair as alt
from st_aggrid import AgGrid

# set page title
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.title('Cuyahoga County 2009-2019')
st.subheader('Click any Column Header to Sort')

# load data into a pandas dataframe
data = 'db_clean.csv'

df = pd.read_csv(data, index_col=None)
df['Case Year'] = df['Case Year'].astype(str)
st.session_state.df = df

# agg_df = df.groupby(['Case Year', 'Case Type']).size().reset_index(name='Count')
# AgGrid(df)
st.write(df)