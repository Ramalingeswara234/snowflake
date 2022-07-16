import streamlit;
import pandas;
import snowflake.connector;
import requests;


streamlit.title('my new diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blue Berry Oat Meal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Rango Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some Fruits', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):    
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
  
def get_fruit_load_list():
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    return my_cur.fetchall()
  

# write your own comment -what does the next line do? 
streamlit.header("Fruityvice Fruit Advice!")
try: 
  fruit_choice = streamlit.text_input("what fruit would you like the information about ?",'kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    streamlit.write("The user entered input is ", fruit_choice)
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)


    #my_data_row = my_cur.fetchone()
    #streamlit.text("Hello from Snowflake:")
    #streamlit.text(my_data_row)
 
    # add a button to load the fruit
    if streamlit.button("Get Fruit load list"):
      my_cnx = snowflake.connector.connect(**streamlist.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
    streamlist.stop()
    fruit_choice = streamlit.text_input("What fruit would you like to add ?",'kiwi')
    streamlit.write("Thanks for adding ", fruit_choice)
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('"+ fruit_choice + "')")
                 
except URLError as e:
   streamlit.error();
  
