import streamlit;
import pandas;
import snowflake.connector;
import requests;
from urllib.error import URLError

streamlit.title('my new diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blue Berry Oat Meal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Rango Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets put a pick list here
fruits_selected = streamlit.multiselect('Pick some Fruits', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table on the page
streamlit.dataframe(fruits_to_show)

 
# Create the repetable code block called function
def get_fruitvice_data(this_fruit_choice):    
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# new section to display Fruitvice API Response
streamlit.header("Fruityvice Fruit Advice!")
try: 
  fruit_choice = streamlit.text_input("what fruit would you like the information about ?")
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    streamlit.write("The user entered input is ", fruit_choice)
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)  
except URLError as e:
   streamlit.error();
    
streamlist.header("The Fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor as my_cur:
    my_cur.execute("Select * from fruit_load_list")
    return my_cur.fetchall()


# add a button to load the fruit
if streamlit.button("Get Fruit load list"):
  my_cnx = snowflake.connector.connect(**streamlist.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)     

 # allow the end user to add a fruit to the list 
 def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('"+ fruit_choice + "')")
    return "Thanks for adding" + new_fruit

 add_my_fruit = streamlit.text_input(" What fruit would you like to add ?")
 if streamlit.button("Add a Fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_fm_function)
 my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
  


  
  
