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

    st.session_state['attendees'] = dh.multiple_text_submission_box(8, 6)

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

    # if 'attendees' not in st.session_state:
    #      = attendees

    st.write(st.session_state['attendees'])

    assign_helper = utils.key_shuffle(len(st.session_state['attendees']))
    st.write(assign_helper)

    if len(st.session_state['attendees']) < 6:
        cannot_assign = True
        st.write('Go back to previous tab and submit your attendees.')
        st.button(
            "Go back",
            on_click=dh.switch_tab, 
            args=("pasta_tabs", "Attendee list")
        )
    else:
        cannot_assign = False

    magic_button = st.button(
        "Assign!", 
        on_click=None,
        disabled=cannot_assign)

    if magic_button:

        pasta_people = utils.return_pasta_characters_from_yml(st.session_state['attendees'])
        st.write(pasta_people)
        # st.write(type(pasta_people))
        
        # for key in pasta_people.keys():
        #     st.write(key)
        #     st.write(pasta_people[key])