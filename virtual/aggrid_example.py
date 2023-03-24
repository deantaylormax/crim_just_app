from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder


df = pd.read_csv('virtual/db_clean.csv')

AgGrid(
    df.head(50),
    gridOptions=GridOptionsBuilder.from_dataframe(df).build(),
)