import streamlit as st
from matplotlib import image
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "me.jpeg")
st.title("About Me")
st.snow()
img = image.imread(IMAGE_PATH)
st.image(img,width=90)

st.write("Hey! I am Meghana Shivani Gogu, a self-motivated and Industrious individual who is extremely passionate about the field of Data Science, currently seeking opportunities that help me learn, and aid in my career advancement. You can know me more through LinkedIn (url: https://www.linkedin.com/in/meghana-shivani/)")
