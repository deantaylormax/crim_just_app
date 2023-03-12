import streamlit as st

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.write("# Defense Attorney Data")
import streamlit as st
import pandas as pd
ß
# Create sample DataFrame with two columns
data = pd.DataFrame({
    'Country': ['USA', 'USA', 'USA', 'Canada', 'Canada', 'Mexico'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Toronto', 'Vancouver', 'Mexico City']
})

# Get list of unique countries in DataFrame
countries = data['Country'].unique()

# Create first dropdown for selecting a country
selected_country = st.selectbox('Select a country', countries)

# Filter DataFrame to get cities in selected country
cities = data[data['Country'] == selected_country]['City'].unique()

# Create second dropdown for selecting a city in the selected country
selected_city = st.selectbox('Select a city', cities)

# Display selected country and city
st.write('You selected:', selected_city, 'in', selected_country)




# st.sidebar.success("Select a demo above.")

