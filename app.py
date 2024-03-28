import pandas as pd
import streamlit as st
import plotly.express as px


data = pd.read_csv('wines_SPA.csv')

st.title('Discover Your Perfect Spanish Wine!')
st.subheader('Explore and find the ideal Spanish wine based on your preferences')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
  'https://flomaster.top/uploads/posts/2022-06/1654793533_63-flomaster-club-p-vino-risunok-karandashom-krasivo-80.jpg',
   "wine_image.png")

img = Image.open("wine_image.png")
st.image(img, caption='Select your parameters below')

price_range = st.slider(
     "What is your budget range?",
     value=(4, 3200))

actual_range = list(range(price_range[0], price_range[1]+1))

high_rating = st.checkbox('Only show highly rated wines')

if high_rating:
    filtered_data = data[data.price.isin(actual_range) & (data.rating >= 4.5)]
else:
    filtered_data = data[data.price.isin(actual_range)]

st.write('Explore wines categorized by price and rating')

fig = px.scatter(filtered_data, x="price", y="rating")           
st.plotly_chart(fig)

st.write('Distribution of acidity for filtered wines')
fig2 = px.histogram(filtered_data, x="acidity")
st.plotly_chart(fig2)

st.write('Here are some recommended wines')
st.dataframe(filtered_data.sample(40))

st.write('Explore the relationship between the year of the wine and the number of reviews')
fig3 = px.bar(filtered_data, x="year", y="num_reviews", title="Number of Reviews vs. Wine Year")
st.plotly_chart(fig3)
