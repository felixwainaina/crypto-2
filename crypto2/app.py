
import pickle
import streamlit as st

import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from pygments.lexers import go

st.set_page_config(page_icon="🗠", page_title="Cryptocurrency Overview", layout="centered", initial_sidebar_state="auto")

st.sidebar.image(
    "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/z3ahdkytzwi1jxlpazje",
    width=50,
)

c1, c2 = st.columns([1, 8])

with c1:
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/chart-increasing_1f4c8.png",
        width=90,
    )

st.markdown(
    """# **Crypto Overview**
Cryptocurrency price app
"""
)

st.header("**Selected Crypto Price**")
# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
def chart(real,predicted,show=True):
    plt.plot(real,color='g')
    plt.plot(predicted,color='r')
    plt.ylabel('BTC/USD')
    plt.xlabel("9Minutes")
    plt.savefig("chart.png")
    if show:plt.show()


# defining the function which will make the prediction using the data which the user inputs
