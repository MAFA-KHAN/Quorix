# mindlock_app.py

import streamlit as st
import random
import time

# ------------------
# PAGE CONFIG
# ------------------
st.set_page_config(
    page_title="MIND.LOCK",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------
# CUSTOM CSS
# ------------------
st.markdown("""
    <style>
        body {
            background-color: black;
        }
        .main {
            background-color: black;
            color: red;
        }
        h1, h2, h3, h4, h5, h6, .stText, .stButton > button {
            color: red;
        }
        footer {
            text-align: center;
            color: #888;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 0.9em;
            color: #ff0000;
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------
# SIDEBAR NAV
# ------------------
menu = st.sidebar.radio("Navigate", ["Home", "Explore", "About", "Feedback"])

# ------------------
# PAGE: HOME
# ------------------
if menu == "Home":
    st.markdown("<h1 style='text-align: center;'>MIND.LOCK</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Unlock the truth of your subconscious</h4>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="center-button">
            <form action="#game">
                <button style="background-color: red; color: white; padding: 10px 20px; font-size: 16px; border: none;">Let's Play Game</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

# ------------------
# PAGE: EXPLORE
# ------------------
elif menu == "Explore":
    st.title("🧠 Psychological Levels in MIND.LOCK")
    levels = [
        ("Boot Test", "Your mind boots... but does it obey?"),
        ("Memory Cage", "Repeat the unseen, recall under pressure."),
        ("The Loop", "Break the pattern, or live in it."),
        ("The Mirror", "Do your choices reflect your truth?"),
        ("Impulse Hit", "React before you think — or fail."),
        ("The Philosophical Kill", "One wrong belief, and it ends."),
        ("Your Core", "Final trial — are you real, or code?")
    ]
    for title, desc in levels:
        st.subheader(f"🔻 {title}")
        st.markdown(f"*{desc}*")

# ------------------
# PAGE: ABOUT
# ------------------
elif menu == "About":
    st.title("👁️ About MIND.LOCK")
    st.markdown("""
    **MIND.LOCK** is a Gen Z anime-inspired psychological test in the form of a dark web simulation.
    It dives deep into your subconscious through levels that simulate pressure, deception, memory traps, and belief illusions.

    Built using beginner Python logic, it's not just a game — it's a statement.
    """)

# ------------------
# PAGE: FEEDBACK
# ------------------
elif menu == "Feedback":
    st.title("📨 Feedback")
    name = st.text_input("Your Name")
    thoughts = st.text_area("What did you think of MIND.LOCK?")
    if st.button("Submit"):
        st.success("Feedback submitted. Thank you for playing with your mind.")

# ------------------
# GAME PAGE SECTION
# ------------------
st.markdown("""
    <div id="game">
""", unsafe_allow_html=True)

def glitch_text(text):
    st.markdown(f"<h3 style='color:red;'>{text}</h3>", unsafe_allow_html=True)
    time.sleep(1)

def memory_level():
    sequence = [random.randint(10, 99) for _ in range(3)]
    st.write("Memorize this sequence:", sequence)
    time.sleep(4)
    st.empty()
    ans = st.text_input("Enter the sequence (space separated):")
    if ans:
        user_seq = [int(x) for x in ans.split()]
        if user_seq == sequence:
            st.success("Passed Level")
            return True
        else:
            st.error("Failed")
            return False

# ------------------
# MAIN GAME START
# ------------------
if menu == "Home":
    st.subheader("Level 1: BOOT")
    if st.button("BOOT SYSTEM"):
        glitch_text("Booting...")
        glitch_text("Mind.SYS Detected")
        glitch_text("Loading Level 2")

        st.subheader("Level 2: MEMORY CAGE")
        passed = memory_level()
        if passed:
            st.balloons()
            st.success("Level 3: THE LOOP")
            user = st.text_input("Are you stuck in a loop? Type YES to escape.")
            if user.lower() == "yes":
                st.success("You escaped.")

                st.subheader("Level 4: THE MIRROR")
                mirror = st.radio("Choose one:", ["I lie", "I tell truth"])
                if mirror:
                    st.success("Interesting... Moving on.")

                    st.subheader("Level 5: IMPULSE HIT")
                    impulse = st.text_input("Type RED as fast as you can!")
                    if impulse.upper() == "RED":
                        st.success("Fast enough.")

                        st.subheader("Level 6: PHILOSOPHICAL KILL")
                        belief = st.radio("Does morality exist without humanity?", ["Yes", "No"])
                        st.success("Belief registered")

                        st.subheader("Level 7: YOUR CORE")
                        core = st.text_input("Who are you really?")
                        if core:
                            st.markdown("### Calculating personality...")
                            time.sleep(2)
                            st.markdown("## You are a reflective introvert, hacker-minded, truth-seeker.")
                            st.markdown("### But nothing is real.")
                            glitch_text("BREAKING...")
                            glitch_text("\\\\\\\\\\ SCREEN CRACKED //////////")

# ------------------
# FOOTER
# ------------------
st.markdown("""
    <div class="footer">
        @ 2025MIND.LOCK | POWERED BY MAFA
    </div>
""", unsafe_allow_html=True)
