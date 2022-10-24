import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Yimin Zhou')

df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
medianhousevalue = st.slider('Median Housing Price:', 0.0, 500001.0, 3.6)  # min, max, default

st.subheader('See more filters in the side bar')

# create a multi select
location_type = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults top 3 countries in population


df = df[df.median_house_value <= medianhousevalue]


df = df[df.ocean_proximity.isin(location_type)]

level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Median', 'High')
)
if level =='Low':
    df = df[df.median_income <= 2.5]
elif level =='Median':
    df = df[df.median_income > 2.5 & df.median_income <= 4.5]
elif level =='High':
    df = df[df.median_income > 4.5]

# show on map
st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20,15))
df.median_house_value.hist(bins=30)
st.pyplot(fig)



