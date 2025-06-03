# app_streamlit.py
import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title='BFMCPC AI Tools', layout='wide')

st.title('BFMCPC Background Remover & Image Enhancer')

file = st.file_uploader('Upload an image', type=['png','jpg','jpeg'])
if file:
    img = Image.open(file)
    st.image(img, caption='Original Image', use_column_width=True)
    # Background Remover
    input_bytes = file.read()
    removed = remove(input_bytes)
    img_removed = Image.open(io.BytesIO(removed))
    st.image(img_removed, caption='Background Removed', use_column_width=True)
    # Download buttons
    st.download_button('Download Removed BG', data=removed, file_name='no_bg.png', mime='image/png')
