import streamlit as st
from cbe_image import fetch_image
from cbe_doc import fetch_doc_names
import requests
import base64
from io import BytesIO
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF
from PIL import Image

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

st.title("All CBE student profiles image")

student_id = st.text_input("Enter Student ID:",placeholder="eg.02.9585.21.01.2021")
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


doc_names = fetch_doc_names()
st.title(f"Over '{len(doc_names)}' Student DOCS")
selected_doc = st.selectbox("Select Document:", doc_names, placeholder="Choose a document...")
if selected_doc:
    doc_url = URL + selected_doc
    if selected_doc.lower().endswith('.pdf'):
        try:
            response = requests.get(doc_url)
            if response.status_code == 200:
                # Convert PDF to images using PyMuPDF
                pdf_document = fitz.open(stream=response.content, filetype="pdf")
                
                st.write(f"**{selected_doc}** - {len(pdf_document)} pages")
                
                # Add page navigation
                if len(pdf_document) > 1:
                    page_num = st.slider("Select Page", 1, len(pdf_document), 1) - 1
                else:
                    page_num = 0
                
                # Render selected page as image
                page = pdf_document.load_page(page_num)
                mat = fitz.Matrix(2, 2)  # 2x zoom for better quality
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("png")
                
                # Display the page as image
                st.image(img_data, caption=f"Page {page_num + 1}", use_container_width=True)
                
                pdf_document.close()
                
                # Download button
                st.download_button(
                    label="Download PDF",
                    data=response.content,
                    file_name=selected_doc,
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error displaying PDF: {e}")
            # Fallback to download only
            response = requests.get(doc_url)
            if response.status_code == 200:
                st.download_button(
                    label="Download PDF",
                    data=response.content,
                    file_name=selected_doc,
                    mime="application/pdf"
                )

        # response = requests.get(doc_url)
        # if response.status_code == 200:
        #     st.download_button(
        #         label="Download PDF",
        #         data=response.content,
        #         file_name=selected_doc,
        #         mime="application/pdf"
        #     )
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