# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Cyber Awareness", page_icon="/static/1.png")
st.title('CYBER AWARENESS.')
st.subheader('Statistics on Kenya cyber crimes.')
 

#st.image('hacker.gif', width =400)
#st.image('Cyber-Security-sector-statistics-Report-Q2-FY-2020-2021-03.jpg', width=400)
#st.image('Cyber-Security-sector-statistics-Report-Q2-FY-2020-2021-04.jpg', width=400)
#st.image('Cyber-Security-sector-statistics-Report-Q2-FY-2020-2021-05.jpg', width=400)
#st.image('Cyber-Security-sector-statistics-Report-Q2-FY-2020-2021-06.jpg', width=400)

sunset_imgs = [
    'static/cyberattacks-at-a-glance.gif',
    'static/0622-gates-after-a-cyber-defense-breach.gif',
    'static/1.png',
    'static/2.png',
    'static/3.png',
    'static/4.png',
    'static/5.png',
    'static/6.png',
    'static/7.png',
    'static/8.png',
]

st.image(sunset_imgs, width=400)
st.sidebar.success("PAGES")


import streamlit as st 

#st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")