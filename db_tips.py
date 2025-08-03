import streamlit as st
import pandas as pd

from db import run_query

def get_db_tips():
    return run_query("select", "HOWTO", ["onderwerp", "databanktips"], order="id")

databanktips = get_db_tips()
st.table(databanktips.data)
