import streamlit as st
#import os

#st.write(os.listdir())

with open("Capture.PNG", "rb") as file:
    btn = st.download_button(
        label="google first PL",
        data=file,
        file_name="image.png",
        mime="image/png"
    )
