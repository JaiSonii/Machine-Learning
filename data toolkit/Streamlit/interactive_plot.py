import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.header('Altair Scatter Chart')

chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a', y = 'b', size= 'c' , tooltip= ['a','b','c','d','e'])
st.altair_chart(chart)

st.header('Interactive Charts')

st.subheader('Line Chart')
df = pd.read_csv('C:\Machine Learning\data toolkit\Streamlit\csv\lang_data.csv')
lang_list = df.columns.to_list()
lang_choices = st.multiselect('Select Languages', lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader('Area Chart')
st.area_chart(new_df)

st.header('Data Visualalization with Plotly')
st.subheader('Display the Data Frame')
df = pd.read_csv(r"C:\Machine Learning\data toolkit\Streamlit\csv\tips.csv")
st.dataframe(df)

st.subheader('Pie Chart')
fig = px.pie(df, values= 'total_bill', names = 'day')
st.plotly_chart(fig)

st.subheader('Pie Chart with multiple parameters')
fig = px.pie(df, values= 'total_bill', names ='day', opacity= .7, color_discrete_sequence= px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('Histogram')

x1 = np.random.randn(200)+1
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2

hist_data = [x1, x2, x3]
hist_labels = ['Group - 1','Group - 2','Group - 3']
fig = ff.create_distplot(hist_data, hist_labels , bin_size=[0.1,0.25,0.5])
st.plotly_chart(fig)