import requests
import json
import streamlit as st
import pandas as pd



def get_prediction(data={"num_countries":0,"years_school":9.5,"height":4.165}):
  url = 'https://askai.aiclub.world/2bd98a94-4b74-42d4-be2b-0d25c7acc91b'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  return response

#creating the web app

#title
st.title("Age Project")#change the title according to your project

#dashboard
st.subheader("User Dashboard")

#change the input variables as your training data
num_countries = st.slider("Num_countries",0,9,5)
years_in_school = st.slider("Number of years in the school", 0,20,5)
height = st.slider("Your Height",2.00,7.00,4.00)

#input_data dictionary keys must be exactly same as the column_names of the dataframe
input_data = {
    "num_countries": num_countries,
    "years_school": years_in_school,
    "height": height

}

#user data
st.subheader("User Data")
st.dataframe(pd.DataFrame(input_data, index = [0]))

#predicting
prediction = get_prediction(input_data)
who_am_i = json.loads(json.loads(prediction)['body'])['predicted_label']

st.subheader("Predictions")
if who_am_i == 'child':
    st.write("you are a **Child**")
else:
    st.write("You are an **Adult**")
