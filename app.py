import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])

import google.generativeai as genai
import os 
import streamlit as st 

os.environ["GOOGLe_API_KEY"]="AIzaSyCX4gQ8qjCLShyfeRVJfn_Y6vJBZ93VHUo"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")

st.title("AI Search")
input_text=st.text_input("Search the topic you want")

if input_text:
  response=model.generate_content(input_text)
  st.write(response.text)

## http://192.168.29.104:8501
