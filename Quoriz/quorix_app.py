import streamlit as st
import random
import time

# ---------------------------
# Config & Styling
# ---------------------------
st.set_page_config(page_title="MIND.LOCK", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: black;
        color: red;
    }
    .centered-button button {
        display: block;
        margin: auto;
        background-color: #e63946;
        color: white;
        border-radius: 10px;
        padding: 1em 2em;
        font-size: 1.5em;
        transition: all 0.3s ease;
    }
    .glitch-title {
        font-size: 48px;
        color: #e63946;
        text-align: center;
        animation: glitch 1s infinite;
    }
    @keyframes glitch {
      0% {text-shadow: 2px 2px red;}
      50% {text-shadow: -2px -2px white;}
      100% {text-shadow: 2px 2px red;}
    }
    footer {
        text-align: center;
        margin-top: 4em;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Initialize Session State
# ---------------------------
if "username" not in st.session_state:
    st.session_state.username = ""
if "level" not in st.session_state:
    st.session_state.level = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

# ---------------------------
# Sidebar Navigation
# ---------------------------
nav = st.sidebar.radio("Navigate", ["Home", "Explore", "About", "Feedback"])

# ---------------------------
# Home Page
# ---------------------------
if nav == "Home":
    st.markdown("<div class='glitch-title'>MIND.LOCK</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Decode Your Darkness</h4>", unsafe_allow_html=True)
    
    username_input = st.text_input("Enter your codename:")
    if username_input:
        st.session_state.username = username_input

    if st.session_state.username:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class='centered-button'>
            <form action="/?nav=Explore">
                <button type="submit">Let's Play Game</button>
            </form>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# Explore Page (Levels)
# ---------------------------
elif nav == "Explore":
    st.title("Welcome, {}".format(st.session_state.username or "Player"))
    st.subheader("Levels")

    levels = ["Level 1: Memory Cage", "Level 2: Mirror Maze", "Level 3: Fragment Truth", "Level 4: The Core", "Level 5: Identity Leak"]

    for i, lvl in enumerate(levels):
        if st.session_state.level >= i+1:
            if st.button(lvl):
                st.session_state.selected_level = i + 1
                st.experimental_rerun()
        else:
            st.button(lvl, disabled=True)

    # Triggered level logic
    if "selected_level" in st.session_state:
        if st.session_state.selected_level == 1:
            st.header("Level 1: MEMORY CAGE")
            sequence = [random.randint(10,99) for _ in range(3)]
            st.write("Memorize this sequence:")
            st.code("""[
0:{}
1:{}
2:{}
]""".format(sequence[0], sequence[1], sequence[2]))
            
            user_input = st.text_input("Enter the sequence (space separated):")
            if user_input:
                expected = "{} {} {}".format(sequence[0], sequence[1], sequence[2])
                if user_input.strip() == expected:
                    st.success("✅ Passed! Moving to Level 2")
                    st.session_state.level = 2
                    st.session_state.score += 10
                    del st.session_state.selected_level
                    st.experimental_rerun()
                else:
                    st.error("❌ Failed. Try again.")

# ---------------------------
# About Page
# ---------------------------
elif nav == "About":
    st.title("About MIND.LOCK")
    st.markdown("""
    **MIND.LOCK** is a Gen Z–inspired, glitch-aesthetic psychological game built in Python.
    Designed with a black and red theme, each level reveals hidden aspects of your cognition.

    **Tech Stack:** Python, Streamlit, HTML/CSS-injected UI.

    **Creator:** MAFA | Built for modern minds 🧠
    """)

# ---------------------------
# Feedback Page
# ---------------------------
elif nav == "Feedback":
    st.title("Give Your Feedback")
    feedback = st.text_area("What do you think of MIND.LOCK?")
    if st.button("Submit Feedback"):
        if feedback:
            st.session_state.feedbacks.append(feedback)
            st.success("Thanks for the feedback!")

    st.subheader("Previous Feedback")
    for i, fb in enumerate(st.session_state.feedbacks):
        st.markdown(f"**{i+1}.** {fb}")

# ---------------------------
# Footer
# ---------------------------
st.markdown("""<footer>@ 2025MIND.LOCK | POWERED BY MAFA</footer>""", unsafe_allow_html=True)

