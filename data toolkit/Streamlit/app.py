import streamlit as st

st.title('This is the Title')
st.header('This is Header')
st.subheader('This is SubHeader')
st.text('This is text')

st.markdown('- # Using Markdown')
st.markdown('# Makrdown\n## Markdown \n### Markdown \n#### Markdown \n Markdown')

st.markdown('- ## Using write')
st.write('range(0,10)')
st.write(range(1,10))

st.subheader('Writing Code')
st.code('''if age < 18: 
    print('You not move')\n''')


st.success('This is a success message')
st.warning('This is a warning message')
st.error(ZeroDivisionError('This is zero division error message'))
st.exception(ZeroDivisionError('This is zero division exception'))

st.markdown('- ## Some more functions and interactions')
if st.button('click Me'):
    st.write('! You clicked me')

st.markdown('- ## Using checkbox')
    
st.checkbox('Checkbox1')
st.checkbox('Checkbox2')

st.subheader('Using radio buttons')
gender = st.radio('Select gender', ['male', 'female'])
if gender:
    st.write(f'You are a {gender}')

volume = st.slider('Volume', 0, 100)
st.write('Volume ', volume)

st.markdown('- ## Using select box')
degree = st.selectbox('Degree', ['Btech','BCA','MCA','Mtech','Chai Tapri'])
st.write(f'You have selected {degree}')

st.markdown('- ## Using multi-select box')
skills = st.multiselect('Skills',['Machine Learning', 'Data Analytics','NextJS','HTML','CSS','JavaScript','ReactJS','Rust','Python','Java'])
st.write('You have selected', len(skills), 'skills')

st.markdown('- ## Using form')
username = st.text_input('Username', value='')
st.write(f'Hi {username}')

password = st.text_input('Password', type = 'password')

st.text_area('Description', height=5, placeholder='Please Describe YourSelf')

st.date_input('Enter your DOB')

st.time_input('Enter your birth time',)

st.number_input('Your Age',18,110)

