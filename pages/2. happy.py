import streamlit as st
from matplotlib import image
import pandas as pd
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "image.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "world_happiness_report.csv")

st.title(":blue[Happiness] :orange[Analysis] :smiley:")
st.balloons()

img = image.imread(IMAGE_PATH)
st.image(img,width=300)

st.write("Being happy all the time may take a bit of work, as life has this funny habit of throwing lemons at you at the most inopportune time. Yet, happiness is a choice. You have the option to let those lemons topple you to the ground, or you could catch some, make a lemonade and get a profit out of it. Let's just see the happiness rank of various countries across the world.")

df = pd.read_csv(DATA_PATH)

st.dataframe(df)
st.bar_chart(df, x='Country', y='Happiness Rank')