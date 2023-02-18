import streamlit as st
import requests
import numpy as np
from streamlit_lottie import st_lottie
from PIL import Image
import cv2


st.set_page_config(page_title="Main Page",page_icon=":tada:",layout="wide")

def lottie_load(url :str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#Inserting lottie animations

lottie=lottie_load("https://assets5.lottiefiles.com/packages/lf20_gkgqj2yq.json")

img_link1=Image.open(r'C:\Users\kadal\Documents\HAXIOS\Images\pic1.jpg')
img_link2=Image.open(r'C:\Users\kadal\Documents\HAXIOS\Images\pic2.jpg')


#Adding local CSS files

def local(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        
    
local(r'C:\Users\kadal\Documents\HAXIOS\Style\content.css')



#organises the code
with st.container():
    st.subheader("Hi :wave:, This is an app to predict the rate of alzymer disease in humans")
    st.title("This deep learning neural network model runs on VGG 16 architecture")
    st.write("Powered by python")

    st.write("Learn more with python")
    st.write("[Learn More>](https://vtopcc.vit.ac.in/vtop/login)")


with st.container():
    st.write("---") #divider
    left_column,right_column=st.columns(2)  #inserting 2 columns
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        Alzheimer's disease is the most common type of dementia. It is a progressive disease beginning with mild
        memory loss and possibly leading to loss of the ability to carry on a conversation and respond to the environment.
        Alzheimer's disease involves parts of the brain that control thought, memory, and language.""")

        st.write("[Click here to learn more>](https://www.mayoclinic.org/diseases-conditions/alzheimers-disease/symptoms-causes/syc-20350447)")
        
    with right_column:
        #insert the animation
        st_lottie(lottie,height=300,key="Perfect Cure")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)

    with left_column:
        st.header("How do we plan to implement this")
        st.write('##')
        st.write("Do you want to check if you have alzymers disease??")
        st.write("This can be done by a single click of the mouse and 1 image upload")
    with right_column:
        st.write("Click here to checkout whether you have alzymers disease")
        res=st.button("Click here")
        if res:
            st.write(":smile:")
            uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "csv","png"])

            if uploaded_file is not None:
    # Process the uploaded file
                #contents = uploaded_file.read()
                img=Image.open(uploaded_file)
                st.write("You uploaded the following file:")
                st.image(img,"Uploaded_Image")
                

with st.container():
    st.write("--")
    st.header("How deadly is the disease")
    st.write("##")
    img_col,text_col=st.columns((1,2))  #tex t column is twice as big as image


    with img_col:   #inserting images
        st.image(img_link1)
        st.image(img_link2)

    with text_col:
        st.write(
            """
It is the fifth leading cause of death for adults aged 65 and older, and the seventh leading cause of death for all adults.
Alzheimer's disease involves partsof the brain that control thought, memory, and language, and, over time,
can seriously affect a person's ability to carry out daily activities.""")

    #link to videos
    st.markdown("Watch video...](https://www.youtube.com/watch?v=7F-t9yvPP_0)")
    
#__CONTACT BLOCK__

with st.container():
    st.write("--")  #divider
    st.header("Contact Us") 
    st.write("##") #extra space


    contact_form="""
    <form action="https://formsubmit.co/srinidhi.k2021@vitstudent.ac.in" method="POST">

    <input type="hidden" name="_capta" value="false">
     <input type="text" name="name" placeholder="Your name"required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your Message here" required></textarea>
    
     <button type="submit">Send</button>
    </form>
    """
    left_col,right_col=st.columns(2)

#eject html code into web app
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st.empty()
        
    
    
