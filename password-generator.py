import streamlit as st
import random

char_set_1 = '~```! @#$%^&*()_-+={[}]|\:;"\'<,>.?/'
char_set_1_mobile_friendly = '`!@$&*()-:;",.?/'
char_set_2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

st.title('🔑 Password Generator')

col1, col2 = st.columns(2)

with col1:
    is_mobile = st.checkbox('Mobile Friendly', value=True)
    length = st.slider('Password length', value=10, max_value=20)

with col2:
    chosen_set = char_set_1_mobile_friendly if is_mobile else char_set_1
    char_set_1 = st.text_input('Special Characters', value=chosen_set)
    char_set_2 = st.text_input('Numbers and Letters', value=char_set_2)

password_space = char_set_1 + char_set_2

def generate_password(space, length):
    for _ in range(length):
        yield random.SystemRandom().choice(space)

st.info(''.join(generate_password(password_space, length)))



st.write('[The Python Guide .com](https://thepythonguide.com)')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
