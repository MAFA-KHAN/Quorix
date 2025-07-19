import streamlit as st
import time
import random

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="MIND.LOCK",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>
body {
    background-color: #000000;
    color: #ffffff;
}
header, footer {visibility: hidden;}
.css-1v0mbdj {padding-top: 3rem;}
.main {
    background-color: #000;
    color: #fff;
    font-family: 'Courier New', monospace;
}
h1, h2, h3 {
    color: #e63946;
    text-align: center;
}
.stButton>button {
    background-color: #e63946;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("### @ 2O25MIND.LOCK | POWERED BY MAFA")
st.markdown("# 🧠 MIND.LOCK")
st.markdown("### _A Psychological Terminal Game to Break Your Thinking._")

# ---------------------------
# SESSION STATE
# ---------------------------
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'started' not in st.session_state:
    st.session_state.started = False

# ---------------------------
# LEVELS
# ---------------------------
def level_1():
    st.subheader("LEVEL 1 — SYSTEM BOOT")
    if st.button("Initiate System"):
        st.session_state.level += 1

def level_2():
    st.subheader("LEVEL 2 — MEMORY TEST")
    st.write("REMEMBER THIS: **OBSIDIAN**")
    time.sleep(2)
    st.session_state.level += 1

def level_3():
    st.subheader("LEVEL 3 — DISTRACTION")
    st.text_input("What is 9 x 3?", key="q1")
    st.radio("Choose a color:", ["Red", "Blue"], key="q2")
    word = st.text_input("What was the first word?")
    if word:
        if word.strip().upper() == "OBSIDIAN":
            st.success("🧠 MEMORY INTACT.")
        else:
            st.error("🪫 MEMORY CORRUPTED.")
        st.session_state.level += 1

def level_4():
    st.subheader("LEVEL 4 — THE LOOP")
    ans = st.text_input("How do you escape a loop?")
    if ans:
        if "break" in ans.lower():
            st.success("Correct. But what if the loop is your mind?")
        else:
            st.warning("Incorrect. You are still looping.")
        st.session_state.level += 1

def level_5():
    st.subheader("LEVEL 5 — IDENTITY FOLD")
    sec = st.text_input("Type a secret no one knows.")
    if sec:
        st.write("...\nOthers have confessed the same thing.")
        st.write("You are not unique.")
        st.session_state.level += 1

def level_6():
    st.subheader("LEVEL 6 — DO YOU EXIST?")
    start = time.time()
    ans = st.text_input("You have 4 seconds to type: `I EXIST`")
    end = time.time()
    if ans:
        if ans.strip().upper() == "I EXIST" and (end - start) <= 4:
            st.success("You exist.")
        else:
            st.error("Too slow. You hesitate to exist.")
        st.session_state.level += 1

def level_7():
    st.subheader("LEVEL 7 — HUMAN CONFIRMATION")
    human = st.text_input("Are you human?")
    if human:
        st.write("Prove it. Say something no AI can ever say.")
        final = st.text_input("Type it:")
        if final:
            st.write("...\nAnalyzing...\n...")
            time.sleep(2)
            st.warning("Not enough. You are not convincing.")
            st.session_state.level += 1

def level_8():
    st.subheader("LEVEL 8 — BROKEN TIME")
    times = ["14:92", "25:61", "00:00", "13:13", "09:66"]
    choice = st.radio("Choose the real time:", times)
    if st.button("Lock Answer"):
        if choice == "00:00":
            st.success("Correct.")
        else:
            st.error("Incorrect.")
        st.session_state.level += 1

def level_9():
    st.subheader("LEVEL 9 — CODE SHIFT")
    msg = st.text_input("Decode this: `Uifsf jt op tqppo`")
    if msg:
        if msg.lower().strip() == "there is no spoon":
            st.success("🧠 You see beyond code.")
        else:
            st.error("Wrong. You still see the matrix.")
        st.session_state.level += 1

def level_10():
    st.subheader("LEVEL 10 — FINAL SEQUENCE")
    st.write("You have reached the core...")
    st.write("Decrypting...")
    time.sleep(2)
    st.markdown("<h1 style='color:#e63946;text-align:center;font-size:50px;'>SYSTEM BREACHED</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>The mind is no longer yours.</h2>", unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    glitch = random.choice([
        "⛔🧠💀 SYSTEM FAILURE 💀🧠⛔",
        "███▓▒░ GLITCH DETECTED ░▒▓███",
        "⚠️ FRACTURE IN MEMORY ZONE ⚠️",
        "🔴🔴🔴 FATAL THOUGHT LEAK 🔴🔴🔴",
        "ERROR: /mind/reality/core.py"
    ])
    st.markdown(f"<h3 style='text-align:center;color:red;'>{glitch}</h3>", unsafe_allow_html=True)
    st.markdown("<hr><center style='color:#aaa'>@ 2O25MIND.LOCK | POWERED BY MAFA</center>", unsafe_allow_html=True)

# ---------------------------
# GAME FLOW
# ---------------------------
if not st.session_state.started:
    if st.button("Start Game"):
        st.session_state.started = True
else:
    levels = {
        1: level_1,
        2: level_2,
        3: level_3,
        4: level_4,
        5: level_5,
        6: level_6,
        7: level_7,
        8: level_8,
        9: level_9,
        10: level_10
    }
    current = st.session_state.level
    if current in levels:
        levels[current]()
