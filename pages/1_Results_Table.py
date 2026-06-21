import streamlit as st
from utils import search_apps

st.title("Search Apps")

query = st.text_input("Enter search term")

if st.button("Search"):

    df = search_apps(query)

    st.dataframe(df)

    st.session_state["results"] = df