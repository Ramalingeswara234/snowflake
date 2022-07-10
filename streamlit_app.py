import streamlit;
import pandas;

streamlit.title('my new diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blue Berry Oat Meal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Rango Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect('pick some fruits', list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

