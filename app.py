import streamlit as st
from cbe_image import fetch_image
import requests

st.title("CBE Image Downloader")

student_id = st.text_input("Enter Student ID:")
if student_id:
    image_url = fetch_image(student_id)
    if image_url =='not found':
        st.image('https://media.tenor.com/swTDQJ85dDEAAAAM/aaaa.gif')
        st.error(f"Student ID: {student_id} Not found.")
    else:
        st.image(image_url, caption=f"Student ID: {student_id}")
        response = requests.get(image_url)
        if response.status_code == 200:
            st.download_button(
                label="Download Image",
                data=response.content,
                file_name=f"{student_id}.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("Failed to download image.")