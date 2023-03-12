import streamlit as st
import numpy as np 
import altair as alt
import pandas as pd
from resources import totals, button_mkr

st.write("JUDICIAL DATA")
tab1 = 'Total Cases by Judge'
tab2 = 'Total By Charge'
tab3 = 'Exploratory Data Analysis'
tab_lst = [tab1, tab2, tab3]
tab1, tab2, tab3 = st.tabs(tab_lst)
df = st.session_state.df #gets data from Home


with tab1:
    by_judge = df.groupby('Judge').size().reset_index(name='Total Cases')
    options = st.multiselect(
    'Choose',
    by_judge.Judge.unique())
    # st.write('You selected:', options)
    judge_filter = by_judge[by_judge.Judge.isin(options)]
    judge_filter.sort_values(by='Total Cases', ascending=False, inplace=True)
    st.write(judge_filter)

    chart = alt.Chart(judge_filter).mark_bar().encode(
        x=alt.X('Judge', sort=alt.EncodingSortField(field='Total_Cases', order='descending')),
        y='Total Cases'
    )

    # # display data labels above the bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text='Total Cases'
    )
    # display chart in the app with data labels
    st.altair_chart(chart + text, use_container_width=True)
    btn = button_mkr(judge_filter, key=1)


def charter(df, group_col, count_name, new_col, type='size'):
    if type != 'size':
        df_g = df.groupby(group_col).agg({type: 'mean'}).reset_index()
    df_g = df.groupby(group_col).size().reset_index(name=count_name)
    df_g = df_g.rename(columns={group_col: new_col})
    # df_g.group_col.rename(columns={group_col: new_col}, inplace=True)
    # df_g.sort_values(by=count_name, ascending=False, inplace=True)
    options = st.multiselect(
    'Choose',
    df_g[new_col].unique())
    # st.write('You selected:', options)
    filter = df_g[df_g[new_col].isin(options)]
    filter.sort_values(by=count_name, ascending=False, inplace=True)
    st.write(filter.style.hide_index())
    chart = alt.Chart(filter).mark_bar().encode(
        x=alt.X(new_col, sort=alt.EncodingSortField(field=count_name, order='descending')),
        y=count_name
    )
    # # display data labels above the bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text=count_name
    )
    # display chart in the app with data labels
    return st.altair_chart(chart + text, use_container_width=True)
    
with tab2:
    charter(df, 'charge_desc', 'Total', 'Charge')
    

with tab3:
    # Create dependent dropdowns
    judge = sorted(df['Judge'].unique())
    judge = st.selectbox('Select a judge', judge)
    def_lst = df[df['Judge'] == judge]['Defense Attorney'].unique()
    def_atty = st.selectbox('Select a defense attorney', def_lst)
    filtered_df = df[(df['Judge'] == judge) & (df['Defense Attorney'] == def_atty)]
    filtered_df.drop(columns=['Judge', 'Defense Attorney'], inplace=True)
    # st.csv_downloader(filtered_df, 'my_data.csv')
    st.write(filtered_df)
    
# with tab4:
#     # Create sample DataFrame with two columns
#     data = pd.DataFrame({
#         'Country': ['USA', 'USA', 'USA', 'Canada', 'Canada', 'Mexico'],
#         'City': ['New York', 'Los Angeles', 'Chicago', 'Toronto', 'Vancouver', 'Mexico City']
#     })

#     # Get list of unique countries in DataFrame
#     countries = data['Country'].unique()

#     # Create first dropdown for selecting a country
#     selected_country = st.selectbox('Select a country', countries)

#     # Filter DataFrame to get cities in selected country
#     cities = data[data['Country'] == selected_country]['City'].unique()

#     # Create second dropdown for selecting a city in the selected country
#     selected_city = st.selectbox('Select a city', cities)

#     # Display selected country and city
#     st.write('You selected:', selected_city, 'in', selected_country)
