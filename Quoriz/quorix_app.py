import streamlit as st

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="MIND.LOCK", layout="centered", initial_sidebar_state="expanded")

# ------------------------
# Session State Init
# ------------------------
if "level" not in st.session_state:
    st.session_state.level = 1

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ------------------------
# Sidebar Navigation
# ------------------------
with st.sidebar:
    st.markdown("## 🧠 MIND.LOCK")
    nav = st.radio("Navigate", ["Home", "Explore", "About", "Feedback"])
    if nav:
        st.session_state.current_page = nav

# ------------------------
# Footer
# ------------------------
def footer():
    st.markdown("""<div style='text-align: center; padding: 30px 0; color: gray; font-size: 14px;'>
    <hr style="border-color:#ff0000;">
    @ 2025 MIND.LOCK | POWERED BY MAFA
    </div>""", unsafe_allow_html=True)

# ------------------------
# Level Functions
# ------------------------
def level_1():
    st.title("Level 1: DECISION HAZE")
    st.write("You're standing in a dark alley. Two doors: 🔴 Red or ⚫ Black.")
    choice = st.radio("Choose a door", ["Red", "Black"])
    if st.button("Enter"):
        if choice == "Black":
            st.success("Correct. You passed Level 1.")
            st.session_state.level = max(st.session_state.level, 2)
        else:
            st.error("Wrong door. You failed Level 1.")

def level_2():
    st.title("Level 2: MEMORY CAGE")
    sequence = [20, 96, 83]
    st.write("Memorize this sequence:")
    st.code("[\n0:20\n1:96\n2:83\n]")
    user_input = st.text_input("Enter the sequence (space separated):")
    if st.button("Submit"):
        if user_input.strip() == "20 96 83":
            st.success("Correct. You passed Level 2.")
            st.session_state.level = max(st.session_state.level, 3)
        else:
            st.error("Incorrect. You failed Level 2.")

def level_3():
    st.title("Level 3: REACTION SNAP")
    st.write("You hear a sound. React fast.")
    if st.button("CLAP"):
        st.success("Fast reflex! You passed Level 3.")
        st.session_state.level = max(st.session_state.level, 4)

def level_4():
    st.title("Level 4: TRUTH VEIL")
    q = st.radio("You see a stranger drop a wallet. Do you return it?", ["Yes", "No"])
    if st.button("Decide"):
        if q == "Yes":
            st.success("Good conscience. Passed Level 4.")
            st.session_state.level = max(st.session_state.level, 5)
        else:
            st.error("Failed. Try again.")

def level_5():
    st.title("Level 5: CORE MIND")
    q = st.text_area("Who are you, really?")
    if st.button("Reveal Truth"):
        st.markdown("### 🤖 Analysis Complete")
        st.write("You are a deep thinker, possibly introverted, with analytical leanings.")
        st.markdown("#### Final Verdict: Welcome to your subconscious.")
        st.markdown("""
            <div style='color:red; font-size:30px; text-align:center; margin-top:40px;'>
                ⚠️ SYSTEM OVERLOAD ⚠️<br>
                <span style='font-family:monospace;'>GL!TCH_0x000F9</span>
                <br><br>
                <span style='font-size:50px;'>💥</span>
            </div>
        """, unsafe_allow_html=True)

# ------------------------
# Page Content Functions
# ------------------------
def home_page():
    st.markdown("<h1 style='text-align:center; color:white;'>MIND.LOCK</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:red;'>Enter Your Subconscious.</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Let's Play Game"):
        st.session_state.current_page = "Explore"
    st.markdown("</div>", unsafe_allow_html=True)

def explore_page():
    st.title("🧠 Explore Levels")
    for i in range(1, 6):
        if st.session_state.level >= i:
            if st.button(f"Enter Level {i}"):
                st.session_state.current_page = f"Level_{i}"
        else:
            st.button(f"🔒 Level {i}", disabled=True)

def about_page():
    st.markdown("""
    ### About MIND.LOCK
    **MIND.LOCK** is a psychological web game that challenges your inner instincts, memory, decision-making, and ethical reasoning.  
    Designed with a black-red anime aesthetic, the game progresses through 5 mind-altering levels—each one deeper than the last.
    
    🧪 *Built using Python + Streamlit with futuristic UI powered by Gen Z culture.*

    👩‍💻 Created by: **MAFA**
    """)

def feedback_page():
    st.markdown("### 💬 Feedback")
    st.text_area("What did you feel during the game?")
    st.text_input("Your Email (optional)")
    st.button("Submit")

# ------------------------
# Router
# ------------------------
def route():
    if st.session_state.current_page == "Home":
        home_page()
    elif st.session_state.current_page == "Explore":
        explore_page()
    elif st.session_state.current_page == "About":
        about_page()
    elif st.session_state.current_page == "Feedback":
        feedback_page()
    elif st.session_state.current_page == "Level_1":
        level_1()
    elif st.session_state.current_page == "Level_2":
        level_2()
    elif st.session_state.current_page == "Level_3":
        level_3()
    elif st.session_state.current_page == "Level_4":
        level_4()
    elif st.session_state.current_page == "Level_5":
        level_5()
    else:
        st.write("404 Page Not Found")

# ------------------------
# App Start
# ------------------------
route()
footer()
