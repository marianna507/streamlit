import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.subheader('Map analysis')
st.text("""The following maps are analysis done on the cyber attacks Victims in Kenya. 
Nairobi and Kiambu had the highest number of cyber victims reported both in 2020 
and 2021. Gender count shows that in most counties more number of females reported
than males which suggest that females are suspectible to be cyber victims""")

sunset_imgs = [
    'static/cyber victims 2020.png',
    'static/cyber victims 2021.png',
    'static/density computation.png' ,
    'static/hotspot analysis.png',
    'static/gender.png',
    'static/financial fraud.png',
    'static/phishing.png',
    'static/spam.png',
    'static/malware.png',
]
st.image(sunset_imgs, width=400)
