import streamlit as st
import pandas as pd
from scrapers.rasathane import get_json_data

eq_data = pd.DataFrame(get_json_data())

st.write(
    """
    # Introduction

    I've created this repo to present a minimal crisis map for earhquakes in Turkey.
    Thanks for [BOGAZICI UNIVERSITY KANDILLI OBSERVATORY AND EARTHQUAKE RESEARCH INSTITUTE (KOERI)](http://www.koeri.boun.edu.tr/scripts/lasteq.asp) sharing the data.

    **Upon use of our data, proper attribution should be given to KOERI-RETMC in scientific articles and general purpose reports by referencing the network citation.**

    # Docker Image on the Hub
    
    Explore Image on Docker Hub: [mebaysan/turkey-earthquake-crisis-app](https://hub.docker.com/repository/docker/mebaysan/turkey-earthquake-crisis-app)

"""
)

st.write(eq_data)
