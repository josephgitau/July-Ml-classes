import streamlit as st
import pandas as pd
import numpy as np

# app title
st.title('Dev streamlit app')

# app description
st.write('This web app demonstrates all the components of streamlit')

# Dataframe magic method 
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['a', 'b', 'c'])
df
st.caption('This is a dataframe using the magic method')
st.write(df)
st.caption('This is a dataframe using the write method')
st.table(df)
st.caption('This is a dataframe using the table method')
st.dataframe(df.style.highlight_max(axis=0))
st.caption('This is a dataframe highlighting the max value in each column')

# Line chart
chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-1.292066, 36.821945],
    columns=['lat', 'lon'])

st.map(map_data)

# bar chart: st.bar_chart()
# area chart: st.area_chart()
# scatter chart: st.scatter_chart()

# widgets

# slider
st.slider('Select a range of values', 0, 100, (25, 75))

# button 
if st.button('Say hello'):
    st.write('Why hello there')

# button to ridirect to a link
if st.button('Africdsa'):
    st.write('Redirecting to Google')
    st.write('https://www.africdsa.com')

# select box
list_of_fruits = ['apple', 'banana', 'orange']
st.selectbox('Select a fruit', list_of_fruits)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

if st.sidebar.button('Say helloss'):
    st.write('Why hello there')

import time

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'