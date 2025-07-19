import streamlit as st
import random
import json
import os

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="MIND.LOCK", layout="wide")

# -------------------------------
# Initial Session State
# -------------------------------
if "username" not in st.session_state:
    st.session_state.username = ""
if "level_unlocked" not in st.session_state:
    st.session_state.level_unlocked = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "results" not in st.session_state:
    st.session_state.results = {}
if "bg_music" not in st.session_state:
    st.session_state.bg_music = False

# -------------------------------
# Save Feedback to File
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
# Navigation Buttons
# -------------------------------
st.sidebar.title("MIND.LOCK")
if st.sidebar.button("🏠 Home"):
    st.session_state.current_page = "Home"
if st.sidebar.button("🧠 Explore"):
    st.session_state.current_page = "Explore"
if st.sidebar.button("📖 About"):
    st.session_state.current_page = "About"
if st.sidebar.button("💬 Feedback"):
    st.session_state.current_page = "Feedback"
st.sidebar.checkbox("🎵 Glitch Music", key="bg_music")

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
# HOME PAGE
# -------------------------------
if st.session_state.current_page == "Home":
    st.markdown("""
        <div style='text-align:center; margin-top:100px;'>
            <h1 style='color:#e63946; font-family:monospace;'>MIND.LOCK</h1>
            <h3 style='color:#fff; font-style:italic;'>Unlock the psyche. Or be trapped within.</h3>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Let's Play Game", key="lets_play_home"):
        st.session_state.current_page = "Explore"

    footer()

# -------------------------------
# EXPLORE PAGE
# -------------------------------
if st.session_state.current_page == "Explore":
    st.title("🧠 Levels")
    for i in range(1, 11):
        col1, col2 = st.columns([0.85, 0.15])
        if st.session_state.level_unlocked >= i:
            with col1:
                st.markdown(f"### 🔓 Level {i}")
            with col2:
                if st.button(f"Enter {i}", key=f"enter_{i}"):
                    st.session_state.current_level = i
                    st.session_state.current_page = f"Level{i}"
        else:
            with col1:
                st.markdown(f"### 🔒 Level {i} (Locked)")
    footer()

# -------------------------------
# ABOUT PAGE
# -------------------------------
if st.session_state.current_page == "About":
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
if st.session_state.current_page == "Feedback":
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
# LEVEL LOGIC (DIVERSE)
# -------------------------------
def level_page(level_num):
    st.title(f"🧩 Level {level_num}")

    tasks = {
        1: ("Introvert vs Extrovert", "Choose your comfort zone:", ["Quiet library", "Loud concert"]),
        2: ("Logic or Emotion?", "A close friend is in trouble. What do you trust more?", ["Gut feeling", "Careful analysis"]),
        3: ("Pattern Trap", "Which shape completes the sequence?", ["◼️", "🔺", "⚫", "⬟"]),
        4: ("Impulse Control", "You found a red button. Do you press it?", ["YES!", "Better wait"]),
        5: ("Memory Recall", "Memorize this sequence:", [random.randint(10, 99) for _ in range(5)]),
        6: ("Identity Crisis", "Pick what feels *more you*:", ["Dreamer", "Doer", "Observer"]),
        7: ("Paranoia Simulation", "You hear whispers. Trust your mind or instincts?", ["Mind", "Instincts"]),
        8: ("Order vs Chaos", "Your room is:", ["Organized", "Messy chaos"]),
        9: ("Thought vs Action", "Which defines you more?", ["Thoughts", "Actions"]),
        10: ("Final Glitch", "Are you the watcher or the watched?", ["Watcher", "Watched"])
    }

    title, question, options = tasks[level_num]
    st.subheader(f"🕶️ {title}")
    st.markdown(f"**{question}**")

    if level_num == 5:
        st.session_state[f"sequence_{level_num}"] = options
        st.code(" ".join(map(str, options)))
        user_input = st.text_input("Enter sequence:", key=f"input_{level_num}")
        if st.button("Submit", key=f"submit_{level_num}"):
            try:
                user_seq = list(map(int, user_input.strip().split()))
                if user_seq == options:
                    st.success("🧠 Perfect memory!")
                    st.session_state.level_unlocked = max(st.session_state.level_unlocked, level_num + 1)
                    st.session_state.results[f"Level {level_num}"] = "Passed"
                    st.session_state.current_page = "Explore" if level_num < 10 else "Summary"
                else:
                    st.error("Wrong sequence.")
                    st.session_state.results[f"Level {level_num}"] = "Failed"
            except:
                st.error("Please enter valid numbers.")
    else:
        choice = st.radio("Select:", options, key=f"radio_{level_num}")
        if st.button("Lock Choice", key=f"submit_{level_num}"):
            st.success("Choice recorded.")
            st.session_state.level_unlocked = max(st.session_state.level_unlocked, level_num + 1)
            st.session_state.results[f"Level {level_num}"] = choice
            st.session_state.current_page = "Explore" if level_num < 10 else "Summary"

    footer()

# -------------------------------
# RENDER LEVELS
# -------------------------------
for i in range(1, 11):
    if st.session_state.current_page == f"Level{i}":
        level_page(i)

# -------------------------------
# SUMMARY PAGE
# -------------------------------
if st.session_state.current_page == "Summary":
    st.title("🔮 Final Personality Summary")
    st.markdown("You've reached the end of MIND.LOCK. Here's what your mind revealed:")
    st.json(st.session_state.results)
    st.balloons()
    st.success("You survived the mind trap.")
    footer()

