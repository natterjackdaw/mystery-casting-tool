import streamlit as st


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
    if 'cleaned_inputs' not in st.session_state:
        st.session_state.cleaned_inputs = []

    inputs = []
    for i in range(max_entries):
        name = st.text_input(
            label=f"Name {i+1}",
            max_chars=40,
            key=f"name_{i+1}",
            help="Please enter name/nickname of person you need to assign a character to."
        )
        if name:
            inputs.append(name)

    st.write(inputs)
    st.session_state.cleaned_inputs = [n for n in inputs if len(n) > 0]
    st.write(st.session_state.cleaned_inputs)

    if len(st.session_state.cleaned_inputs) > min_entries:
        disable_submit = False
    else:
        disable_submit = True

    if st.button("Assign everyone!"):
        return st.session_state.cleaned_inputs