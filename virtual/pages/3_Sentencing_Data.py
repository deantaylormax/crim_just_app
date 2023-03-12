import streamlit as st
import pandas as pd
import csv
from resources import charter, charter_avg, button_mkr, charter_avg2
import altair as alt
st.write("# Sentencing Data")
df = st.session_state.df #gets data from Home
# df1, chart, btn, option = charter_avg2(df, 'charge_desc','Charge Type', 'Prison Years')


race_g = df.groupby(['charge_desc', 'Race']).agg({'Prison Years': 'mean'}).reset_index()
option = st.selectbox(
    'Choose Offense Type(s)',
    race_g['charge_desc'].unique())


#average for all races by charge type
#charge average
ch_avg_data = df[df['charge_desc'] == option]
ch_avg = ch_avg_data['Prison Years'].mean().round(2)
# st.write(ch_avg)
# charge_avg = df.groupby('charge_desc').agg({'Prison Years': 'mean'}).reset_index()
# st.write(f'this is the charge average {charge_avg}')
filter = race_g[race_g['charge_desc'] == option]
filter['Prison Years'] = filter['Prison Years'].astype(int).round(2)
filter.sort_values(by='Prison Years', ascending=False, inplace=True)
#add a row to the filter dataframe that has the ch_avg data
new_row = {'charge_desc': option, 'Race': 'AVERAGE', 'Prison Years': ch_avg}
filter = filter.append(new_row, ignore_index=True)

chart = (
    alt.Chart(filter)
    .mark_bar()
    .encode(
        alt.X('Race'),
        alt.Y('Prison Years'),
        color=alt.condition(
        alt.datum.Race == 'AVERAGE',
        alt.value('red'),
        alt.value('black')
    )
    ).properties(width=500, height=300, title='Average Sentence by Race and Charge Type').interactive())
text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text='Prison Years (Average)'
    )
labels = (
    alt.Chart(filter)
    .mark_text(dx=0, dy=15, color='white', align='center', baseline='middle')
    .encode(
        alt.X('Race'),
        alt.Y('Prison Years'),
        text='Prison Years'
    )
    )
st.altair_chart(chart + labels, use_container_width=True)
# st.write(filter)
btn2 = button_mkr(filter, 2)