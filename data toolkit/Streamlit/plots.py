import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.header('Charts with Random Numbers')
x = pd.DataFrame(np.random.randn(20,3), columns = ['line-1','line-2','line-3'])
st.line_chart(x)

st.subheader('Area Chart')
st.area_chart(x)

st.subheader('Bar Chart')
st.bar_chart(x)

st.header('Visualization with Matplotlib and Seaborn')
st.subheader('Loading the DataFrame')
df = pd.read_csv("C:\Machine Learning\data toolkit\Streamlit\csv\iris.csv")
st.dataframe(df)

st.subheader('Distribution Plot')
fig = plt.figure(figsize=(15,8))
df['variety'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution using seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader('Multiple Graphs')

col1, col2 = st.columns(2)

with col1:
    col1.subheader('KDE False')
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'], kde= False)
    st.pyplot(fig1)

with col2:
    col2.subheader('Hist False')
    fig2 = plt.figure()
    sns.distplot(df['sepal_width'], kde= True, hist= False)
    st.pyplot(fig2)

st.subheader('Changing the Styles')
col1, col2 = st.columns(2)

with col1:
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'], kde= False)
    st.pyplot(fig1)

with col2:
    sns.set_theme(context='poster', style='darkgrid')
    fig2 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_width'], kde= True, hist= False)
    st.pyplot(fig2)
    
st.subheader('Scatter Plot')

fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

df = pd.read_csv('C:\Machine Learning\data toolkit\Streamlit\csv\iris.csv')
st.subheader('Count Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data  = df, x = 'variety')
st.pyplot(fig)

st.subheader('Box Plot')
fig = plt.figure(figsize=(15,8))
sns.boxplot(data = df, x = 'variety', y = 'sepal_length')
st.pyplot(fig)

st.subheader('Violin Plot')
fig = plt.figure(figsize=(15,8))
sns.violinplot(data = df, x = 'variety', y = 'sepal_length')
st.pyplot(fig)