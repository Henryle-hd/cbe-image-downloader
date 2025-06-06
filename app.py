import streamlit as st
from cbe_image import fetch_image
from cbe_doc import fetch_doc_names
import requests

from dotenv import load_dotenv
import os

load_dotenv()
URL=os.getenv("DOC_URL")

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

st.title("Public Student DOCS")
doc_names = fetch_doc_names()
selected_doc = st.selectbox("Select Document:", doc_names)
if selected_doc:
    doc_url = URL + selected_doc
    if selected_doc.lower().endswith('.pdf'):
        st.markdown(f'<embed src="{doc_url}" type="application/pdf" width="100%" height="800px">', unsafe_allow_html=True)
        response = requests.get(doc_url)
        if response.status_code == 200:
            st.download_button(
                label="Download PDF",
                data=response.content,
                file_name=selected_doc,
                mime="application/pdf"
            )
    elif selected_doc.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        st.image(doc_url)
        response = requests.get(doc_url)
        if response.status_code == 200:
            st.download_button(
                label="Download Image",
                data=response.content,
                file_name=selected_doc,
                mime="image/jpeg"
            )