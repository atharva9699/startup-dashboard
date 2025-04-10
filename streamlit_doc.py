
import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')

st.header('I am learning Streamlit')

st.subheader('Atharva Deepak Gondhale')

st.write('This a normal writ text  like paragraph')

st.markdown("""
        # Heading 1  
        ## Heading 2
        ####  heading 4
        * Iam ATHARVA  
        **ATHARVA**  
        *ATHARVA*  
        ***ATHARVA***  
        - Kabaddi
        - Swimming
        - Dance

        1. Kabaddi
        2. Swimming
        3. Dance

""")
st.code("""
    def square(num):
        return num**2
    square(2)

""")

st.latex('x^2+y^2 =z^2')

df = pd.DataFrame({
    'name': ['Atharva', 'Avnish', 'Pradymna'],
    'marks': [80, 90, 85],
    'age': [21, 15, 24]
})
st.dataframe(df)

st.metric('DSA Skills', 'LeetCode', '+100%')
st.json({
    'name': ['Atharva', 'Avnish', 'Pradymna'],
    'marks': [80, 90, 85],
    'age': [21, 15, 24]
})
st.image('my_pic.jpeg')
st.sidebar.title('Files')

col1, col2, col3 = st.columns(3)
with col1:
    st.image('my_pic.jpeg')
with col2:
    st.image('my_pic.jpeg')
with col3:
    st.image('my_pic.jpeg')

st.error('Unkown Error Occurred')
st.success("Login Successful")
st.progress(50)

# taking input
email = st.text_input("Enter email")
number = st.number_input("Enter Phone number")

date = st.date_input('Enter Birth Date')
###########################################################           LOGIN  PAGE ####################################
email = st.text_input('Enter email')
password = st.text_input('Enter Password')
gender = st.selectbox('Select Gender:',['male','female'])
btn = st.button('Login')

if btn:
    if email == 'atharvagondhale111@gmail.com' and password=='1234':

        st.balloons()
        st.write(gender)
    else:
        st.error('Incorrect Email/Password')
########################################################### FILE UPLOADAARR  ####################################

import streamlit as st
import pandas as pd

file = st.file_uploader("Select File")

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())


