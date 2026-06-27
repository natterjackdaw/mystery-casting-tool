import streamlit as st

from faker import Faker


# for fake names
fake = Faker(['it_IT', 'en_US', 'en_IE', 'en_IN', 'en_GB', 'es_MX'])


def multiple_text_submission_box(
        max_entries: int,
        min_entries: int
):
    """
    Enter text in multiple boxes.
    You can only submit if you have entered the minimum.
    max_entries: number of free text boxes
    min_entries: how many need to be filled before you press submit.
    """

    with st.form("pasta_party_people"):

        inputs = {}
        for i in range(max_entries):
            if i >= min_entries:
                default_val = ''
            else:
                default_val = fake.unique.first_name()

            inputs[i] = st.text_input(
                label=f"Name {i+1}",
                value=default_val,
                max_chars=40,
                key=f"name_{i+1}",
                help="Please enter name/nickname of person you need to assign a character to."
            )

        submitted = st.form_submit_button("Submit")
        if submitted:
            values = [v for v in inputs.values() if v != ""]
            st.write(f"Are you happy with your final list of {len(values)}?")
            st.write(', '.join(values))


    # st.write(inputs)
    # st.session_state.cleaned_inputs = [n for n in inputs if len(n) > 0]
    # st.write(st.session_state.cleaned_inputs)

    # if len(st.session_state.cleaned_inputs) > min_entries:
    #     disable_submit = False
    # else:
    #     disable_submit = True

    # if st.button("Assign everyone!"):
    #     return st.session_state.cleaned_inputs