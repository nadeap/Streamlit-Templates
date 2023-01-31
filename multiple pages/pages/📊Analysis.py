import streamlit as st
from PIL import Image

st.title("Data Analyst")

st.markdown("# Welcome to my Streamlit app!")
st.write("Analisis Data XXX")

image = Image.open('img/coba.png')
st.image(image, width=700, caption='Halo Tes Satu Dua Tiga')