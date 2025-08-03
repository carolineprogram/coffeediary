import streamlit as st
import pandas as pd

from db import run_query

def get_db_tips():
    return run_query("select", "HOWTO", ["onderwerp", "databanktips"], order="id")

st.title("☕️Koffie!")

def get_koffie():
    #SELECT ks.naam, kw.waargekocht, kf.flavour
    #FROM koffie_soort as ks
    #LEFT JOIN koffie_winkel kw ON ks.id_winkel = kw.id
    #LEFT JOIN koffie_soort_flavours kfs ON ks.id = kfs.id_soort LEFT JOIN koffie_flavours kf ON kfs.id_flavour = kf.id
    ereturn run_query("select", "koffie_soort", ["naam", "koffie_winkel(waargekocht)", "koffie_soort_flavours!inner(koffie_flavours(flavour))"])


databanktips = get_db_tips()
st.table(databanktips.data)

koffie = get_koffie()
st.dataframe(koffie.data)
    
