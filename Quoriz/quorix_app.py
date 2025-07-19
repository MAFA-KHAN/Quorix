import streamlit as st
import random
import json
import os

# -------------------------------
# Config
# -------------------------------
st.set_page_config(page_title="MIND.LOCK", layout="wide")

# -------------------------------
# Session Init
# -------------------------------
if "username" not in st.session_state:
    st.session_state.username = ""
if "level_unlocked" not in st.session_state:
    st.session_state.level_unlocked = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "current_level" not in st.session_state:
    st.session_state.current_level = None
if "sequence" not in st.session_state:
    st.session_state.sequence = None

# -------------------------------
# Feedback File
# -------------------------------
FEEDBACK_FILE = "feedback.json"

def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    return []

def save_feedback():
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(st.session_state.feedback, f)

# -------------------------------
# Footer
# -------------------------------
def footer():
    st.markdown("""
        <div style='text-align:center; padding:10px; font-size:12px; color:#888;'>
            @ 2025MIND.LOCK | POWERED BY MAFA
        </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
page = st.sidebar.radio("", ["Home", "Explore", "About", "Feedback"], label_visibility="collapsed")
st.session_state.current_page = page

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":
    st.markdown("""
        <div style='text-align:center; margin-top:100px;'>
            <h1 style='color:#e63946; font-family:monospace;'>MIND.LOCK</h1>
            <h3 style='color:#fff; font-style:italic;'>Unlock the psyche. Or be trapped within.</h3>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.username == "":
        st.session_state.username = st.text_input("Enter your codename:")
    else:
        st.markdown(f"<p style='text-align:center; color:#fff;'>Welcome back, <strong>{st.session_state.username}</strong>.</p>", unsafe_allow_html=True)

    go = st.button("Let's Play Game")
    if go:
        st.session_state.current_page = "Explore"
        st.experimental_set_query_params(nav="Explore")
        st.rerun()

    footer()

# -------------------------------
# EXPLORE PAGE
# -------------------------------
if page == "Explore":
    st.title("🧠 Levels")
    for i in range(1, 6):
        col1, col2 = st.columns([0.85, 0.15])
        if st.session_state.level_unlocked >= i:
            with col1:
                st.markdown(f"### 🔓 Level {i}")
            with col2:
                if st.button(f"Enter Level {i}"):
                    st.session_state.current_level = i
                    st.session_state.current_page = f"Level{i}"
                    st.rerun()
        else:
            with col1:
                st.markdown(f"### 🔒 Level {i} (Locked)")
    footer()

# -------------------------------
# ABOUT PAGE
# -------------------------------
if page == "About":
    st.title("🧬 About MIND.LOCK")
    st.markdown("""
    MIND.LOCK is a psychological maze of levels designed to test the depths of your mind.

    Inspired by the dark, glitchy aesthetic of anime and hacker themes, this web-based game takes you through memory puzzles, logic traps, and pattern recognition levels.

    Made for Gen Z by creators who vibe with the digital subconscious. Your mind isn’t ready.
    """)
    footer()

# -------------------------------
# FEEDBACK PAGE
# -------------------------------
if page == "Feedback":
    st.title("💬 Feedback Vault")
    with st.form("feedback_form"):
        name = st.text_input("Your Codename")
        comment = st.text_area("Drop your thoughts...")
        submitted = st.form_submit_button("Submit Feedback")
        if submitted and name and comment:
            st.session_state.feedback.append({"name": name, "comment": comment})
            save_feedback()
            st.success("🧨 Feedback received. Your mind is noted.")
    st.divider()
    st.subheader("📜 Previous Feedback")
    for fb in load_feedback():
        st.markdown(f"**{fb['name']}**: {fb['comment']}")
    footer()

# -------------------------------
# LEVEL 1: MEMORY CAGE
# -------------------------------
if st.session_state.current_page.startswith("Level"):
    level = st.session_state.get("current_level", 1)
    st.title(f"🧩 Level {level}: Memory Cage")

    if level == 1:
        if st.session_state.sequence is None:
            st.session_state.sequence = [random.randint(10, 99) for _ in range(3)]

        st.markdown("Memorize this sequence:")
        st.code("\n".join([f"{i}: {num}" for i, num in enumerate(st.session_state.sequence)]))

        user_seq = st.text_input("Enter the sequence (space separated):", key="mem_input")

        if st.button("Submit Sequence"):
            try:
                user_values = list(map(int, user_seq.strip().split()))
                if user_values == st.session_state.sequence:
                    st.success("🧠 Correct! Proceeding to next level...")
                    st.session_state.level_unlocked = max(st.session_state.level_unlocked, level + 1)
                    st.session_state.sequence = None
                    st.session_state.current_page = "Explore"
                    st.rerun()
                else:
                    st.error("❌ Wrong sequence. Try again.")
            except:
                st.error("❌ Invalid input. Please enter numbers only.")

        footer()
