import streamlit as st
import altair as alt
import random

#makes dl button enabling dl of the filtered data
def button_mkr(df, key):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    # return df.to_csv().encode('utf-8')
    converted_df = df.to_csv().encode('utf-8')

    dl_button = st.download_button(
        label="Download data as CSV",
        data=converted_df,
        file_name='large_df.csv',
        mime='text/csv',
        key=key
    )
    return dl_button


def charter(df, group_col, count_name, new_col, type='size'):
    if type != 'size':
        df_g = df.groupby(group_col).size().mean()
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
    btn = button_mkr(filter)
    return btn, st.altair_chart(chart + text, use_container_width=True), options


def charter_avg(df, group_col, new_col, avg_col, type='agg'):
    df_g = df.groupby(group_col)[avg_col].mean().round(2).reset_index()
    avg_col_new = f'Average {avg_col}'
    df_g = df_g.rename(columns={group_col: new_col, avg_col: avg_col_new})
    df_g.sort_values(by=avg_col_new, ascending=False, inplace=True)
    options = st.multiselect(
    'Choose Offense Type(s)',
    df_g[new_col].unique())
    # st.write('You selected:', options)
    filter = df_g[df_g[new_col].isin(options)]
    filter.sort_values(by=avg_col_new, ascending=False, inplace=True)
    st.write('')

    chart = alt.Chart(filter).mark_bar().encode(
        x=alt.X(new_col, sort=alt.EncodingSortField(field=avg_col_new, order='descending')),
        y=avg_col_new
    )
    # # display data labels above the bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text=avg_col_new
    )
    #choose a random number from 100-1000 to use as a key for the download button
    key = random.randint(100,1000)
    btn = button_mkr(filter, key=key)
    
    return st.write(filter), st.altair_chart(chart + text, use_container_width=True), btn, options

def charter_avg2(df, group_col, new_col, avg_col, type='agg'):  #this version permits only one selection not multiple
    df_g = df.groupby(group_col)[avg_col].mean().round(2).reset_index()
    avg_col_new = f'Average {avg_col}'
    df_g = df_g.rename(columns={group_col: new_col, avg_col: avg_col_new})
    df_g.sort_values(by=avg_col_new, ascending=False, inplace=True)
    option = st.selectbox(
    'Choose Offense Type(s)',
    df_g[new_col].unique())
    # st.write('You selected:', options)
    filter = df_g[df_g[new_col] == option]
    filter.sort_values(by=avg_col_new, ascending=False, inplace=True)
    st.write('')

    chart = alt.Chart(filter).mark_bar().encode(
        x=alt.X(new_col, sort=alt.EncodingSortField(field=avg_col_new, order='descending')),
        y=avg_col_new
    )
    # # display data labels above the bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        text=avg_col_new
    )
    #choose a random number from 100-1000 to use as a key for the download button
    key = random.randint(100,1000)
    btn = button_mkr(filter, key=key)
    
    return st.write(filter), st.altair_chart(chart + text, use_container_width=True), btn, option

def totals(df):
    total_cases = df.shape[0]
    return (f'{total_cases} Cases')
