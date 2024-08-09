from dotenv import load_dotenv
load_dotenv() # load environment variables

import streamlit as st
import os
import google.generativeai as genai


from PIL import Image

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

##FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSES
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="" :
        response=model.generate_content([input,image])
    else:
        response=model.generate_content([image])    
    return response.text

st.set_page_config(page_title = "image demonstrator app " )
st.header("Image demonstrator application powered by Google Gemini | Built by Rishi")
input = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("choose an image..", type=[ "jpg", "jpeg" , "png" ]) 
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit= st.button("Tell me about the image")

## if submit is clicked
if submit:
    response= get_gemini_response(input,image)
    st.subheader("the response is")
    st.write(response)