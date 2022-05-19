import streamlit

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 OMEGA 3 & blueberyy oatmeal')
streamlit.text('🥗Kale, Spnichac & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free Range Egg')
streamlit.text('🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
