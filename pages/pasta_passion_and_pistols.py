import streamlit as st

import src.dashboard_helpers as dh


st.header("Pasta, Passion, and Pistols")

st.text("Enter 6 - 8 names below")

dh.multiple_text_submission_box(8, 6)