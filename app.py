import streamlit as st
from cbe_image import fetch_image
import requests

st.set_page_config(
    page_title="CBE Image Downloader",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://henrylee-hd.vercel.app/',
        'Report a bug': "https://github.com/Henryle-hd/cbe-image-downloader/issues",
        'About': "# CBE Image Downloader\nThis app helps you download student images from CBE database."
    }
)

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