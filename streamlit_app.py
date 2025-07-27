import streamlit as st
import pandas as pd

st.title("☕️Koffie!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


data = pd.DataFrame({
    'Naam': ['1', 'Bob', 'Charlie'],
    'Gekocht': [25, 30, 35],
    'Favours': [85, 90, 78],
    'Brew': ['', '', ''],
})
st.table(data)
    
