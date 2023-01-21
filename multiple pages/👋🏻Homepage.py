import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="wertax0",
    page_icon="👋",
)

st.title("UJI COBA")
st.sidebar.success("result")

image = Image.open('img/coba.png')
st.image(image, width=700, caption='Halo Tes Satu Dua Tiga')

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)