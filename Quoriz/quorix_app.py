import streamlit as st
import random

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="MIND.LOCK", layout="wide")

# -------------------------------
# Initialize State
# -------------------------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'level' not in st.session_state:
    st.session_state.level = 0
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []

# -------------------------------
# Style + Animations (CSS)
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Courier New', monospace;
    }
    .center-button button {
        background-color: #e63946;
        color: white;
        border-radius: 10px;
        font-size: 24px;
        animation: glitch 1s infinite;
    }
    @keyframes glitch {
        0% { transform: skew(-2deg); }
        20% { transform: skew(2deg); }
        40% { transform: skew(-1deg); }
        60% { transform: skew(1deg); }
        80% { transform: skew(-1deg); }
        100% { transform: skew(0); }
    }
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: grey;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("☣️ MIND.LOCK")
nav = st.sidebar.radio("Navigate", ["Home", "Explore", "Feedback", "About"])

# -------------------------------
# Home Page
# -------------------------------
if nav == "Home":
    st.title("")
    st.markdown("<h1 style='text-align: center; color: red;'>MIND.LOCK</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Your Mind Isn’t Safe Anymore...</h3>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
        st.session_state.username = st.text_input("Enter your codename:", key="username")
        if st.button("Let's Play Game"):
            st.session_state.page = 'explore'
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Explore Page
# -------------------------------
elif nav == "Explore" or st.session_state.page == 'explore':
    st.header(f"Welcome, {st.session_state.username}")
    st.subheader("Choose Your Level")

    levels = ["Level 1: MEMORY CAGE", "Level 2: REACTION CHAOS", "Level 3: PERCEPTION TWIST", "Level 4: CHOICE LOCKDOWN", "Level 5: IDENTITY CRACK"]

    for i, lvl in enumerate(levels):
        if i <= st.session_state.level:
            if st.button(lvl):
                st.session_state.page = f'level{i+1}'
        else:
            st.button(f"🔒 {lvl}", disabled=True)

# -------------------------------
# Levels Logic
# -------------------------------
def level1():
    st.title("🔐 LEVEL 1: MEMORY CAGE")
    sequence = [random.randint(10, 99) for _ in range(3)]
    st.write("Memorize this sequence:")
    for idx, val in enumerate(sequence):
        st.text(f"{idx}:{val}")

    user_input = st.text_input("Enter the sequence (space separated):")
    if user_input:
        try:
            user_sequence = list(map(int, user_input.strip().split()))
            if user_sequence == sequence:
                st.success("Correct! Proceeding to next level...")
                st.session_state.level += 1
                st.session_state.page = 'explore'
                st.session_state.score += 10
            else:
                st.error("Incorrect! Try again.")
        except:
            st.error("Invalid input format.")

def level_placeholder(level_num):
    st.title(f"🚧 LEVEL {level_num}: COMING SOON")
    st.write("This level is under construction...")

if st.session_state.page == 'level1':
    level1()
elif st.session_state.page in ['level2', 'level3', 'level4', 'level5']:
    level_placeholder(st.session_state.page[-1])

# -------------------------------
# Feedback Page
# -------------------------------
elif nav == "Feedback":
    st.header("📝 Feedback")
    user_feedback = st.text_area("Leave your thoughts or suggestions:")
    if st.button("Submit Feedback"):
        if user_feedback:
            st.session_state.feedback_list.append((st.session_state.username, user_feedback))
            st.success("Feedback submitted. Thanks!")

    st.subheader("Previous Feedback")
    for user, feedback in st.session_state.feedback_list:
        st.markdown(f"**{user}** said: _{feedback}_")

# -------------------------------
# About Page
# -------------------------------
elif nav == "About":
    st.title("About MIND.LOCK")
    st.markdown("""
        **MIND.LOCK** is a minimalist psychological puzzle game designed in a Gen Z glitch-core aesthetic.
        Test your memory, reaction, perception, and identity through 5 escalating levels.

        Built with Python + Streamlit, it offers:
        - Level-wise brain challenges
        - Score tracking
        - Dark UI & anime hacker vibe
        - Feedback system

        👁️ What lies beneath your thoughts?
    """)

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
    <div class='footer'>
        @ 2025MIND.LOCK | POWERED BY MAFA
    </div>
""", unsafe_allow_html=True)

