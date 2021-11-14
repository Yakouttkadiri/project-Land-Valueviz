import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import pydeck as pdk
import plotly.express as px


Header = st.container()
dataset = st.container()
Features = st.container()
modelTraining = st.container()

	
st.markdown(
      """
	  <style>
     .main {
     color: #6495ED;

     }</style>
      
      """,
      unsafe_allow_html=True
  )

with Header:
	Image = Image.open('logo.png')
	st.image(Image, caption='', width = 220)
	st.caption('Land valueviz is an app that permits to visualize land values data and compare them. All in pure Python..')
	
	
#Data Loading
with dataset:
	st.header('Lets visualize 💫!')
	st.caption('This website is using 2016 and 2020s data')
	st.balloons()

	#Importing Datasets, i choose to work only with 2016 and 2020

	@st.cache
	def load_data1():
		df = pd.read_csv("full_2016.csv")
		return df
	df = load_data1()



	@st.cache
	def load_data2():
		df2 = pd.read_csv("full_2020.csv")
		return df2
	df2 = load_data2()

 


    # This cand lead you to the website from which the datasets are token for additional informations
	st.text(' If you want to learn more you can visit the 🇫🇷 government website  : ')
	if st.button("Take me to their website"):
		st.write("[🇫🇷 www.data.gouv.fr 🇫🇷 ]( https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/)")







    #Datasets

	st.sidebar.write('Select a year to show the data:')
	option_1 = st.sidebar.checkbox('👉 2016 👈')
	option_2 = st.sidebar.checkbox('👉 2020 👈')

	dfsample = df.sample(n=100000)
	if option_1:
		st.write(df.head(1000))
		st.write(' 2016 Data here 👆  ')
		st.caption(' Click on the 💬 on the right to save the chart')

	if option_2:
		st.write(df2.head(1000))
		st.write(' 2020 Data here 👆  ')
		st.caption(' Click on the 💬 on the right to save the chart')

with modelTraining:

	#Bar chart
	st.text(' This is a bar chart showing our data according to each commune')
	
	df = pd.read_csv("full_2016.csv")
	dfsample = df.sample(n=100000)
	code_commune = dfsample['code_commune'].value_counts().head(20)
	st.bar_chart(code_commune )


	df2 = pd.read_csv("full_2020.csv")
	st.caption(' Click on the 💬 on the right to save the chart')
	df2sample = df2.sample(n=100000)
	code_commune = df2sample['code_commune'].value_counts().head(10)
	st.bar_chart(code_commune )
      

	st.text(' Our app aim to visualize 2016 and 2020s data, by comparing mainly between these 2 years')
	st.title(' ** 2016 VS 2020 **')


	#HERE



	st.header('Time to train the model !')
	st.text( 'You got to choose the hyperparameters of the model and see how the perormance change')
	sel_col, disp_col = st.columns(2) 
	max_depth = sel_col.slider( ' Choose a departement ', min_value = 00 , max_value = 101)
    

	df = pd.read_csv("full_2016.csv")
	df['latitude']=pd.to_numeric(df['latitude']) 
	df['longitude']=pd.to_numeric(df['longitude'])
	map_data = df[["latitude", "longitude"]]

	st.map(map_data)






