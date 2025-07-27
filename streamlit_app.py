import streamlit as st
import pandas as pd

st.title("☕️Koffie!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


data = pd.DataFrame({
    'Naam': ['Brazil Catuai Vermelho - filter roast', 
                'Brazil Cerrado Peaberry - filter roast', 'Charlie'],
    'Gekocht': ['Onan', 'Onan', 35],
    'Flavours': ['Hazelnoot, Melkchocolade, Zoete appel, Basilium', 
                'Geroosterde hazelnoot, Bosbes, Cacao', 78],
    'Brew': ['Aeropress', 'Aerpress', ''],
})
st.table(data)
    
