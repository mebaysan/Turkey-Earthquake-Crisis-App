import streamlit as st
import pandas as pd
from scrapers.rasathane import get_json_data
from datetime import datetime
import plotly.graph_objects as go
from enum import Enum


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
EQ_DATA["filter_date"] = pd.to_datetime(EQ_DATA["date"], format="%Y.%m.%d")


is_displayed_raw_data = st.sidebar.selectbox(
    "Would you want to see the raw data?", options=("Yes", "No"), index=0
)

# date filter
min_date = st.sidebar.date_input("Last Date (>=)")

# depth filter
min_depth = float(st.sidebar.text_input("Minimum Depth", 0))

# size filter
min_size = float(st.sidebar.text_input("Minimum Size", 0))

# size category filter
# we use this enum class in the map to set marker size
cat_size = st.sidebar.selectbox("Select category of size", ("MD", "ML", "MW"), 1)

# to map actual size categories and selectbox values
class CAT_SIZE_ENUM(Enum):
    MD = "size_md"
    ML = "size_ml"
    MW = "size_mw"


# Filter data
filtered_data = EQ_DATA[
    (EQ_DATA["filter_date"] >= pd.to_datetime(min_date))
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


fig_highlight_dots = go.Scattermapbox(
    lat=filtered_data["latitude"],
    lon=filtered_data["longitude"],
    mode="markers",
    marker=go.scattermapbox.Marker(
        size=filtered_data[CAT_SIZE_ENUM[cat_size].value] * 6, color="#e63946"
    ),
    name="Highlight Markers",
    opacity=0.5,
    hovertemplate="",
    hoverinfo="none",
)

fig_main_dots = go.Scattermapbox(
    lat=filtered_data["latitude"],
    lon=filtered_data["longitude"],
    mode="markers",
    marker=go.scattermapbox.Marker(
        size=filtered_data[CAT_SIZE_ENUM[cat_size].value] * 3, color="#e63946"
    ),
    text=filtered_data["location"],
    name="Crisis Point",
    hovertemplate="<b>Crisis Point</b><br><br>"
    + '<span style="color: #e63946; font-size: 20px;">⏺</span>Date:<b>%{customdata[0]}</b><br>'
    + "Time: <b>%{customdata[1]} </b><br>"
    + "Location: <b>%{customdata[2]} </b><br>"
    + "Depth: <b>%{customdata[3]} </b><br>"
    + cat_size
    + ": <b>%{customdata[4]} </b><br>",
    customdata=filtered_data[
        ["date", "time", "location", "depth", CAT_SIZE_ENUM[cat_size].value]
    ],
)
map = go.Figure([fig_highlight_dots, fig_main_dots])

map.update_layout(
    hovermode="closest",
    hoverlabel={"bgcolor": "#FFF"},
    mapbox_style="open-street-map",
    showlegend=False,
    mapbox=dict(
        bearing=0,
        center=go.layout.mapbox.Center(lat=38.963745, lon=35.243322),
        pitch=0,
        zoom=4.5,
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
)

st.plotly_chart(map)
