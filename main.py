import streamlit as st

with open("image.PNG", "rb") as file:
    btn = st.download_button(
        label="18",
        data=file,
        file_name="image.png",
        mime="image/png"
    )
