import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

from collections import defaultdict

from db import run_query

def get_db_tips():
    return run_query("select", "HOWTO", ["onderwerp", "databanktips"], order="id")

st.title("☕️Koffie!")

def get_koffie():
    #SELECT ks.naam, kw.waargekocht, kf.flavour
    #FROM koffie_soort as ks
    #LEFT JOIN koffie_winkel kw ON ks.id_winkel = kw.id
    #LEFT JOIN koffie_soort_flavours kfs ON ks.id = kfs.id_soort LEFT JOIN koffie_flavours kf ON kfs.id_flavour = kf.id
    return run_query("select", "koffie_soort", ["naam", "koffie_winkel(waargekocht)", "koffie_soort_flavours(koffie_flavours(flavour))", "koffie_beoordeling(beoordeling)"])


koffie = get_koffie()

processed_data = []

for item in koffie.data:
    naam = item["naam"]
    winkel = item["koffie_winkel"]["waargekocht"] if item["koffie_winkel"] else None
    latitude = item["koffie_winkel"]["latitude"] if item["koffie_winkel"] else None
    longitude = item["koffie_winkel"]["longitude"] if item["koffie_winkel"] else None
    flavours = [flavour["koffie_flavours"]["flavour"] for flavour in item["koffie_soort_flavours"]]
    beoordeling = item["koffie_beoordeling"][0]["beoordeling"] if item["koffie_beoordeling"] else None
    
    processed_data.append({
        "naam": naam,
        "winkel": winkel,
        "flavours": ", ".join(flavours),
        "beoordeling": beoordeling
        })

    df_ligging = pd.DataFrame([
        {
            "lat": latitude,
            "lon": longitude,
            "label": winkel
        }
    ])

st.table(processed_data)

# 3. Display the raw table as requested
st.table(df_ligging)

# 4. Set the initial map view centered around Brussels
view_state = pdk.ViewState(
    latitude=50.8477,
    longitude=4.3572,
    zoom=12,
    pitch=0
)

# 5. Create the layer for the dots
scatterplot_layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[lon, lat]',
    get_color=[255, 0, 0, 160],  # Red dots with transparency
    get_radius=150,               # Radius in meters
    pickable=True
)

# 6. Create the layer for the text labels above the dots
text_layer = pdk.Layer(
    'TextLayer',
    data=df_ligging,
    get_position='[lon, lat]',
    get_text='label',
    get_size=16,
    get_color=[0, 0, 0, 255],     # Black text
    get_alignment_baseline='"bottom"',
    get_pixel_offset=[0, -10]     # Shift text slightly above the dot
)

# 7. Draw the interactive map
st.pydeck_chart(
    pdk.Deck(
        layers=[scatterplot_layer, text_layer],
        initial_view_state=view_state,
        tooltip={"text": "{label}"}  # Adds a hover tooltip showing the store name
    )
)
df = pd.DataFrame(
    np.random.randn(100, 2) / 50 + [50.8477, 7.627], # Centered in Brussel
    columns=['lat', 'lon']
)

# 2. Draw the map
st.map(df)
