import streamlit as st

import math

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

st.title ('Learning how to create graphs with Streamlit')


##############
### DATA #####
##############

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

st.write('Basic EDA of our Data:', 
tips.describe().applymap(lambda x: f"{x:0.1f}"), 'tips data is downloaded from https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')




###################
# Set up main app #
###################

fig_size = (10,6)

#Histogram Total Bill
st.header ('Total Bill Distribution')
fig = plt.figure (figsize=fig_size)
sns.histplot(tips['total_bill'])
st.pyplot(fig)
st.write ('Histogram shows distribution of total bills in our data')


#scatterplot total bill and tip

st.header ('Total bill and tip relationship')
fig = plt.figure (figsize=fig_size)
sns.scatterplot(x ='total_bill', y ='tip', data = tips)
st.pyplot(fig)
st.write('The graph shows how total bill and tip data are related')


#scatterplot total bill, tip and size
st.header ('Total bill, tip and size relationship')
fig = plt.figure (figsize=fig_size)
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='size', size='size', sizes=(10,200))
st.pyplot(fig)
st.write ('The graph shows how the total bill, tip, and size are related. As we can see, the bigger groups tend to spend more money and leave more significant tips')


#relationship between a day and total bill
st.header ('Relationship between total bill and day of a week')
fig = plt.figure (figsize=fig_size)
sns.pointplot(x='day', y='total_bill', data=tips)
st.pyplot(fig)
st.write('We can see on the graph the confidence intervals of the total bill for every day of the week. Also, center points show an average daily bill, the biggest on Sunday.')



st.header ('Relationship between a tip and a day of a week')
fig = plt.figure (figsize=fig_size)
sns.scatterplot(x='tip', y='day', data=tips, hue='sex')
st.pyplot(fig)
st.write('The graph helps to understand if a tip is related to the sex of a customer and a day of a week')



st.header ('Relationship between a total bill and a day of a week')
fig = plt.figure (figsize=fig_size)
sns.boxplot (data = tips, x = 'day', y = 'total_bill', hue='time')
st.pyplot(fig)
st.write ('We can see on the graph that the most number of total bills are fall into 15-25 dollars category with some outliers on certain days')


st.header ('Relationship between tips and time of a day (dinner or lunch)')
fig = plt.figure (figsize=fig_size)
sns.countplot(x='time', data=tips)
st.pyplot(fig)
st.write ('there are much more tips during dinner time than at lunch')


st.header ('Relationship between total bill and a tip of a customer')
fig, axs = plt.subplots(ncols=2, figsize=(12,6)) 
sns.scatterplot(x='total_bill', y='tip', data=tips[tips['sex'] == 'Male'], hue='smoker', ax=axs[1], )
axs[1].set_title('Male')
sns.scatterplot(x='total_bill', y='tip', data=tips[tips['sex'] == 'Female'], hue='smoker', ax=axs[0])
axs[0].set_title('Female')
st.pyplot(fig)
st.write('We can see on the graph how sex and smoking influence tips for male and female customers')

