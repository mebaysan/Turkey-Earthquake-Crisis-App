import streamlit as st
import pandas as pd
from scrapers.rasathane import get_json_data
from datetime import datetime

st.markdown("# Introduction 🎈")
st.write(
    """
    I've created this repo to present a minimal crisis map for earhquakes in Turkey.
    Thanks for [BOGAZICI UNIVERSITY KANDILLI OBSERVATORY AND EARTHQUAKE RESEARCH INSTITUTE (KOERI)](http://www.koeri.boun.edu.tr/scripts/lasteq.asp) sharing the data.

    **Upon use of our data, proper attribution should be given to KOERI-RETMC in scientific articles and general purpose reports by referencing the network citation.**
"""
)

EQ_DATA = pd.DataFrame(get_json_data())
EQ_DATA["date"] = pd.to_datetime(EQ_DATA["date"], format="%Y.%m.%d")

is_displayed_raw_data = st.sidebar.selectbox(
    "Would you want to see the raw data?", options=("Yes", "No"), index=0
)

if is_displayed_raw_data == "Yes":
    st.write("# Raw Data")
    st.write(EQ_DATA)

min_date = st.sidebar.date_input("Last Date (>=)")

st.write(
    """
    # Map of {} => Today
""".format(
        datetime.strftime(min_date, "%d/%m/%Y")
    )
)


filtered_data = EQ_DATA[EQ_DATA["date"] >= pd.to_datetime(min_date)]

