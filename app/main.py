import streamlit as st
import pandas as pd
from scrapers.rasathane import get_json_data
from datetime import datetime
import plotly.graph_objects as go


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


st.markdown("# Introduction ☀️")
st.write(
    """
    I've created this repo to present a minimal crisis map for earhquakes in Turkey.
    Thanks for [BOGAZICI UNIVERSITY KANDILLI OBSERVATORY AND EARTHQUAKE RESEARCH INSTITUTE (KOERI)](http://www.koeri.boun.edu.tr/scripts/lasteq.asp) sharing the data.

    **Upon use of our data, proper attribution should be given to KOERI-RETMC in scientific articles and general purpose reports by referencing the network citation.**
"""
)

# Get data
EQ_DATA = pd.DataFrame(get_json_data())
EQ_DATA["date"] = pd.to_datetime(EQ_DATA["date"], format="%Y.%m.%d")


is_displayed_raw_data = st.sidebar.selectbox(
    "Would you want to see the raw data?", options=("Yes", "No"), index=0
)

# date filter
min_date = st.sidebar.date_input("Last Date (>=)")

# depth filter
min_depth = float(st.sidebar.text_input("Minimum Depth", 0))

# size filter
min_size = float(st.sidebar.text_input("Minimum Size", 0))

# Filter data
filtered_data = EQ_DATA[
    (EQ_DATA["date"] >= pd.to_datetime(min_date))
    & (EQ_DATA["depth"] >= min_depth)
    & (
        (EQ_DATA["size_md"] >= min_size)
        | (EQ_DATA["size_ml"] >= min_size)
        | (EQ_DATA["size_mw"] >= min_size)
    )
]


if is_displayed_raw_data == "Yes":
    st.write("# Raw Data 🗃️")
    st.write(filtered_data)
    csv = convert_df(filtered_data)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="raw_data.csv",
        mime="text/csv",
    )


st.write(
    """
    # Crisis Map 📍
""".format(
        datetime.strftime(min_date, "%d-%m-%Y")
    )
)


fig = go.Figure(
    go.Scattermapbox(
        lat=filtered_data["latitude"],
        lon=filtered_data["longitude"],
        mode="markers",
        marker=go.scattermapbox.Marker(size=14),
        text=filtered_data["location"],
    )
)

fig.update_layout(
    hovermode="closest",
    mapbox_style="open-street-map",
    mapbox=dict(
        bearing=0,
        center=go.layout.mapbox.Center(lat=38.963745, lon=35.243322),
        pitch=0,
        zoom=4.5,
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
)

st.plotly_chart(fig)
