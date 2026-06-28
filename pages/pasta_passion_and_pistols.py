import streamlit as st

import src.dashboard_helpers as dh
import src.get_characters as get_characters
import src.utils as utils


st.header("Pasta, Passion, and Pistols")

st.write("The succulent aroma of home cooked pasta is drifting from New York City's most popular Italian eatery, La Speranza, but something else is heating up the kitchen...cold blooded murder! Restauranteur, Pepi Roni, has been shot in the back with his own pistol. Tonight his family and friends will gather to pay their respects to poor Pepi, but one of the guests won't be shedding any tears.")

tab_names = ["Attendee list", "Character results"]
tab_key = "pasta_tabs"
submission_form, results = st.tabs(
    tab_names,
    key=tab_key,
    on_change=dh.sopranos_quote
)



# first tab
with submission_form:
    st.write("You should have at least 6 people to be the suspects. There are two additional party guest options.")

    st.write("Enter your 6 - 8 names below.")

    if 'attendees' not in st.session_state:
        st.session_state['attendees'] = None

    submitted_attendees = dh.multiple_text_submission_box(
        8, 6, tab_key, tab_names[1], 'attendees'
    )

    if submitted_attendees is not None:
        st.session_state['attendees'] = submitted_attendees


    if st.session_state['attendees'] is None:
        # no one submitted
        not_ready = True
    elif len(st.session_state['attendees']) >= 6:
        # print(st.write(st.session_state['attendees']))
        # we can assign
        not_ready = False
    else:
        # not enough people
        not_ready = True

    if 'attendees' in st.session_state:
        if st.button("Forget submitted names"):
            del st.session_state['attendees']
            st.toast("They're swimming with the fishes.")

# who is who?
with results:

    if 'attendees' not in st.session_state:
        cannot_assign = True
        st.write('No attendees in session')
        st.write('Go back to previous tab and submit attendees.')
        # dh.cannot_assign_button(tab_key)
    elif st.session_state['attendees'] is None:
        st.write(f'Session attendees is {st.session_state['attendees']}')
        cannot_assign = True
        # dh.cannot_assign_button(tab_key)
    elif len(st.session_state['attendees']) < 6:
        cannot_assign = True
        st.write(f'You have only submitted {len(st.session_state['attendees'])}, go back to previous tab and submit attendees.')
        st.write(f"So far: {', '.join(st.session_state['attendees'])}")
        # dh.cannot_assign_button(tab_key)
    else:
        cannot_assign = False
        st.write(f"Are you happy with your final list of {len(st.session_state['attendees'])}")
        st.write(', '.join(st.session_state['attendees']))
        
    with st.container(width='content', horizontal=True):
        dh.cannot_assign_button(tab_key)
        magic_button = st.button(
            "Assign!", 
            # on_click=None,
            disabled=cannot_assign,
            type="primary"
        )
                

    if magic_button:

        with st.spinner(text="Making you an offer you can't refuse..."):

            number_of_attendees = len(st.session_state['attendees'])
            length_of_names = [len(name) for name in st.session_state['attendees']]
            longest_name = max(length_of_names)

            pasta_people = get_characters.pasta_passion_pistols(number_of_attendees)

            assignees = []
            random_assigning_helper = utils.key_shuffle(number_of_attendees)
            for i in random_assigning_helper:
                assignees.append(st.session_state['attendees'][i])

            for i in range(len(assignees)):
                pasta_people[i]["player"] = assignees[i]
                
                cols = st.columns([0.15, 0.85], vertical_alignment="center")
                with cols[0]:
                    st.markdown(f"{assignees[i]}", text_alignment='right')
                with cols[1]:
                    with st.expander(f"{pasta_people[i]['name']}"):
                        st.markdown(f"{pasta_people[i]['summary']}")


