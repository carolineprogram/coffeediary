import streamlit as st
import pandas as pd

from db import run_query

def get_db_tips():
    return run_query("select", "HOWTO", ["onderwerp", "databanktips"], order="id")

st.title("☕️Koffie!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

def get_koffie():
    return run_query("select", "koffie_soort", ["naam", "koffie_winkel(waargekocht)"])

# Define the SQL query
"""
SELECT ks.naam, kw.waargekocht
FROM koffie_soort as ks
LEFT JOIN koffie_winkel kw ON ks.id_winkel = kw.id
"""

# Execute the query
response = supabase.table('koffie_soort').select("naam, koffie_winkel(waargekocht)").execute()




data = pd.DataFrame({
    'Naam': ['Brazil Catuai Vermelho - filter roast', 
                'Brazil Cerrado Peaberry - filter roast', 'Charlie'],
    'Gekocht': ['Onan', 'Onan', 35],
    'Flavours': ['Hazelnoot, Melkchocolade, Zoete appel, Basilium', 
                'Geroosterde hazelnoot, Bosbes, Cacao', 78],
    'Brew': ['Aeropress', 'Aerpress', ''],
})
st.table(data)

databanktips = get_db_tips()
st.table(databanktips.data)

koffie = get_koffie()
st.table(koffie.data)
    
