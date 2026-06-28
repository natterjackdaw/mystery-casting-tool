import streamlit as st

def main():
    st.header("Hello!")

    st.text("""
            The idea behind this tool is so you can assign characters of murder mystery games to your party guests.
            Sound like a terrible idea?
            Yeah, you're probably right.
            """)


    with st.expander("About Pasta, Passion, and Pistols (1995)"):
        st.write("Pasta, Passion & Pistols combines theatrical roleplay, structured clue reveals, and strategic interrogation into an immersive murder mystery evening. With clear pacing, honest questioning, and dramatic flair, your group will uncover secrets, expose motives, and reveal the killer in a night filled with suspense, humor, and Italian flair.")
        st.write("6-8 players")
        if st.button("Assign people for deadly pasta mystery mayhem!"):
            st.switch_page("pages/pasta_passion_and_pistols.py")

    


if __name__ == "__main__":
    main()
