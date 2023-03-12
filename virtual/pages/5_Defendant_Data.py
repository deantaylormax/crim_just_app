import streamlit as st
from resources import charter, charter_avg, button_mkr
import altair as alt




st.write("DEFENDANT DATA")
tab1 = 'Average Bond Amount by Race'
tab2 = 'Bond Comparison by Race'
# tab3 = 'Exploratory Data Analysis'
tab_lst = [tab1, tab2]
tab1, tab2 = st.tabs(tab_lst)
# count_name = 'charges'

with tab1:
    df = st.session_state.df #gets data from Home
    plea_g = df.groupby(['Race','charge_desc'])['Bond Amount'].mean().reset_index()
    #rename columns
    plea_g = plea_g.rename(columns={'Bond Amount': 'Average Bond', 'charge_desc': 'Charge Type'})
    options = st.multiselect('Choose Charge Type',plea_g['Charge Type'].unique())
    #convert average bond to int rounded to two decimal places
    plea_g['Average Bond'] = plea_g['Average Bond'].astype(int)
    plea_g.sort_values(by='Average Bond', ascending=False, inplace=True)
    filter = plea_g[plea_g['Charge Type'].isin(options)]
    filter.sort_values(by='Charge Type', ascending=False, inplace=True)
    st.write(filter.style.hide_index())
    chart = alt.Chart(filter).mark_bar().encode(
        x=alt.X('Charge Type', sort=alt.EncodingSortField(field='Average Bond', order='descending')),
        y='Average Bond'
    )
    # # display data labels above the bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text='Average Bond'
    )
    # display chart in the app with data labels
    btn = button_mkr(filter, 1)
# return btn, st.altair_chart(chart + text, use_container_width=True)

with tab2:
    # Create two columns with st.beta_columns()
    # col1, col2 = st.columns(2)

# Add content to the first column
   
    # st.write('This is the first column')
    race_g = df.groupby(['charge_desc','Race'])['Bond Amount'].mean().reset_index()
    race_g = race_g.rename(columns={'Bond Amount': 'Average Bond', 'charge_desc': 'Charge Type'})
    option = st.selectbox('Choose Charge Category',race_g['Charge Type'].unique())
    race_g['Average Bond'] = race_g['Average Bond'].astype(int).round(2)
    # race_g.sort_values(by=['Charge Type', 'Race', 'Average Bond'], ascending=False, inplace=True)
    filter = race_g[race_g['Charge Type'] == option]
    filter.sort_values(by='Average Bond', ascending=False, inplace=True)
    

# Add content to the second column

    # st.write('This is the second column')
    # st.bar_chart(filter.set_index('Race', 'Charge Type'), width=400, height=400)
    
    chart = (
    alt.Chart(filter)
    .mark_bar()
    .encode(
        alt.X("Race"),
        alt.Y("Average Bond"),
        alt.Color("Charge Type"),
        # alt.Tooltip(["Nucleotide", "Similarities"]),
        )
    .properties(width=500, height=300)
    .interactive())
    
    labels = (
    alt.Chart(filter)
    .mark_text(dx=-15, dy=5, color='white', align='center', baseline='middle')
    .encode(
        alt.X('Race'),
        alt.Y('Average Bond'),
        text='Average Bond'
    )
    )
    final_chart = chart + labels
    st.altair_chart(final_chart)
    st.write(filter)
    # st.write(race_g)
    btn2 = button_mkr(filter, 2)