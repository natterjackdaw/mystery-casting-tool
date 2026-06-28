import streamlit as st

from faker import Faker
from typing import List


# for fake names
fake = Faker(['it_IT', 'en_US', 'en_IE', 'en_IN', 'en_GB', 'es_MX'])


def multiple_text_submission_box(
        max_entries: int,
        min_entries: int,
        tab_key: List[str],
        tab_name: List[str],
        session_state_name: str
) -> List[str]:
    """
    Enter text in multiple boxes.
    You can only submit if you have entered the minimum.
    max_entries: number of free text boxes
    min_entries: how many need to be filled before you press submit.
    """
    with st.form("pasta_party_people"):

        inputs = {}
        for i in range(max_entries):
            
            # if session_state_name not in st.session_state:
            #     if i >= min_entries:
            #         default_val = ''
            #     else:
            #         default_val = fake.unique.first_name()
            # else:
            #     try:
            #         default_val = st.session_state[session_state_name][i]
            #     except:
            #         default_val = ''

            if i >= min_entries:
                default_val = ''
            else:
                default_val = fake.unique.first_name()

            inputs[i] = st.text_input(
                label=f"Name {i+1}",
                value=default_val,
                max_chars=20,
                key=f"name_{i+1}",
                help="Please enter name/nickname of person you need to assign a character to."
            )

        submitted = st.form_submit_button(
            "Submit",
            on_click=switch_tab, 
            args=(tab_key, "Character results"),
            type="primary"
        )
        if submitted:

            if session_state_name in st.session_state:
                del st.session_state[session_state_name]

            values = [v for v in inputs.values() if v != ""]
            return values
        
        else:
            return None


def switch_tab(tabs_key: str, tab_name: str):
    """
    Change tabs
    """
    st.session_state[tabs_key] = tab_name


def sopranos_quote():
    st.toast("You know the deal. No one can be trusted.")


def cannot_assign_button(
        tab_keys: str,
        tab_name: str = "Attendee list"
):

    st.button(
        "Go back",
        on_click=switch_tab, 
        args=(tab_keys, tab_name)
    )