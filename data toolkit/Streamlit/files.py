import streamlit as st

import pandas as pd 

st.subheader("Uploading the CSV file")
dt=st.file_uploader("Upload the CSV file : " , type=["csv" , "xlsx"])

# if dt is not None:
#     st.dataframe(dt)
st.subheader("Loading the CSV file")

if dt is not None:
   csv=pd.read_csv(dt)
   st.table(csv.head())
   
st.subheader("Dealing with images directly")
st.image(r"C:\Users\jaius\OneDrive\Desktop\IMG_2401.JPG") 

st.subheader("Dealing with images while uploading")
img_file=st.file_uploader("Upload the Image file : " , type=["png" , "jpeg"])
if img_file is not None:
   st.image(img_file)  

st.subheader("Working with Videos")
video_file=st.file_uploader("Upload the CSV file : " , type=["mkv" , "mp4"])
if video_file is not None:
    st.video(video_file , start_time=0)


st.subheader("Working with Audios")
audio_file=st.file_uploader("Upload the CSV file : " , type=["wav" , "mp3"])
if audio_file is not None:
    st.audio(audio_file.read())