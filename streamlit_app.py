import streamlit as st
import pandas as pd

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
    return run_query("select", "koffie_soort", ["naam", "koffie_winkel(waargekocht)", "koffie_soort_flavours!inner(koffie_flavours(flavour))"])


koffie = get_koffie()

processed_data = []

for item in koffie.data:
    naam = item["naam"]
    winkel = item["koffie_winkel"]["waargekocht"] if item["koffie_winkel"] else None
    flavours = [flavour["koffie_flavours"]["flavour"] for flavour in item["koffie_soort_flavours"]]

    processed_data.append({
        "naam": naam,
        "winkel": winkel,
        "flavours": ", ".join(flavours)
        })
st.table(processed_data)
