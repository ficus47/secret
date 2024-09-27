import streamlit as st
import os

st.write(os.listdir())

with open("image.png", "rb") as file:
    btn = st.download_button(
        label="18",
        data=file,
        file_name="image.png",
        mime="image/png"
    )
