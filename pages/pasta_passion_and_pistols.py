import streamlit as st

import src.dashboard_helpers as dh
import src.utils as utils


st.header("Pasta, Passion, and Pistols")

st.write("The succulent aroma of home cooked pasta is drifting from New York City's most popular Italian eatery, La Speranza, but something else is heating up the kitchen...cold blooded murder! Restauranteur, Pepi Roni, has been shot in the back with his own pistol. Tonight his family and friends will gather to pay their respects to poor Pepi, but one of the guests won't be shedding any tears.")

submission_form, results = st.tabs(
    ["Attendee list", "Character results"],
    key="pasta_tabs",
    on_change=dh.sopranos_quote
)

# first tab
with submission_form:
    st.write("You should have at least 6 people to be the suspects. There are two additional party guest options.")

    st.write("Enter your 6 - 8 names below.")

    attendees = dh.multiple_text_submission_box(8, 6)

    if len(st.session_state['attendees']) >= 6:
        not_ready = False
    else:
        not_ready = True

    st.button(
        "I'm happy - let's get this party started!",
        on_click=dh.switch_tab, 
        args=("pasta_tabs", "Character results"),
        disabled=not_ready
    )

# who is who?
with results:

    if 'attendees' not in st.session_state:
        st.session_state['attendees'] = attendees

    st.write(st.session_state['attendees'])

    assign_helper = utils.key_shuffle(len(st.session_state['attendees']))
    st.write(assign_helper)

    st.write(utils.return_characters_from_yml('pasta_passion_pistols.yml'))