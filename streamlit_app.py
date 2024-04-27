import streamlit as st
from transformers import pipeline
from PIL import Image
import torch

##BLIP
# Create the caption pipeline
initial_caption = pipeline('image-to-text', model="Salesforce/blip-image-captioning-large")

# Display the image using Streamlit
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    image= Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Generate the caption
if st.button("Generate Caption"):
    captions = initial_caption(image)
    st.write(captions[0]['generated_text'])
