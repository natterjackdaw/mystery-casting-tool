import streamlit as st

import src.dashboard_helpers as dh


st.header("Pasta, Passion, and Pistols")

st.write("The succulent aroma of home cooked pasta is drifting from New York City's most popular Italian eatery, La Speranza, but something else is heating up the kitchen...cold blooded murder! Restauranteur, Pepi Roni, has been shot in the back with his own pistol. Tonight his family and friends will gather to pay their respects to poor Pepi, but one of the guests won't be shedding any tears.")

st.write("You should have at least 6 people to be the suspects. There are two additional party guest options.")

st.write("Enter your 6 - 8 names below.")

dh.multiple_text_submission_box(8, 6)
