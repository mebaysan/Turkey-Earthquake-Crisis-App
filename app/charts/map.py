import plotly.graph_objects as go


def get_crisis_map(_cat_size, _filtered_data):

    fig_highlight_dots = go.Scattermapbox(
        lat=_filtered_data["latitude"],
        lon=_filtered_data["longitude"],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=_filtered_data[_cat_size] * 6, color="#e63946"
        ),
        name="Highlight Markers",
        opacity=0.5,
        hovertemplate="",
        hoverinfo="none",
    )

    fig_main_dots = go.Scattermapbox(
        lat=_filtered_data["latitude"],
        lon=_filtered_data["longitude"],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=_filtered_data[_cat_size] * 3, color="#e63946"
        ),
        text=_filtered_data["location"],
        name="Crisis Point",
        hovertemplate="<b>%{customdata[2]}</b><br><br>"
        + '<span style="color: #e63946; font-size: 20px;">⏺</span>Date:<b>%{customdata[0]}</b><br>'
        + "Time: <b>%{customdata[1]} </b><br>"
        + "Depth: <b>%{customdata[3]} </b><br>"
        + "Size: <b>%{customdata[4]} </b><br>"
        + "<extra></extra>",
        customdata=_filtered_data[["date", "time", "location", "depth", _cat_size]],
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
    return map
