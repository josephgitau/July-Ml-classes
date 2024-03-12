## Streamlit credit scoring web App

# importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
st.set_option('deprecation.showPyplotGlobalUse', False)
import pickle

## Describe our app
st.title('Credit Scoring Web App')
st.write('This is a web app to predict the credit score of a customer')

# add an image banner 
st.image('dataset-cover.jpg', use_column_width=True)

# text her informing users we have widgets on the left hand side
st.warning('Please use the widgets on the left hand side to get the predictions and interact with the dataset')

# importing the dataset
df = pd.read_csv('train.csv')

# data description
st.subheader('Data Description')
total_columns, total_rows = df.shape
st.write(f'The dataset has {total_columns} columns and {total_rows} rows')
st.write('This dataset contains information about customers and their credit score')

# add a check box to show the dataset
st.sidebar.subheader('Show Dataset')
if st.sidebar.checkbox('Show Dataset'):
    st.subheader('Sample of the dataset')
    st.dataframe(df.head())

## Data visualization
    
# create two columns with two different visualizations
# first column
st.subheader('Data Visualization')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Credit Score Distribution')
    fig = plt.figure(figsize=(5,5))
    #sns.barplot(x=df['Credit_Score'].value_counts().index, y=df['Credit_Score'].value_counts())
    st.bar_chart(df['Credit_Score'].value_counts())

with col2:
    st.subheader('Occupation Distribution')
    fig = plt.figure(figsize=(5,5))
    # sns.barplot(x=df['Occupation'].value_counts().index, y=df['Occupation'].value_counts())
    st.bar_chart(df['Occupation'].value_counts())
    plt.xticks(rotation=90)

