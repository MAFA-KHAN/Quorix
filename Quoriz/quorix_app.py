import streamlit as st
import pandas as pd
import datetime

# ------------------ CONFIG & STYLES ------------------
st.set_page_config(page_title="Quorix", layout="centered")

st.markdown("""
<style>
.form-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.form-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 10px;
    color: #4a4a4a;
}
.form-subtitle {
    font-size: 1rem;
    color: #6b6b6b;
    margin-bottom: 20px;
}
@media screen and (max-width: 768px) {
    .form-card { padding: 15px; }
    .form-title { font-size: 1.5rem; }
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION INIT ------------------
if "step" not in st.session_state:
    st.session_state.step = "setup"
    st.session_state.title = ""
    st.session_state.num_questions = 1
    st.session_state.questions = []
    st.session_state.answers = []

# ------------------ STEP: SETUP ------------------
if st.session_state.step == "setup":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-title">🧠 Quorix - Create Your Form</div>', unsafe_allow_html=True)

        st.session_state.title = st.text_input("Enter form title", st.session_state.title)
        st.session_state.num_questions = st.number_input("How many questions?", min_value=1, max_value=10, step=1)

        if st.button("Next"):
            st.session_state.questions = [{"text": "", "type": "text"} for _ in range(st.session_state.num_questions)]
            st.session_state.step = "build"

        st.markdown('</div>', unsafe_allow_html=True)

# ------------------ STEP: BUILD ------------------
elif st.session_state.step == "build":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-subtitle">Write your questions and select types:</div>', unsafe_allow_html=True)

        for i in range(len(st.session_state.questions)):
            st.session_state.questions[i]["text"] = st.text_input(f"Q{i+1}", key=f"qtext_{i}")
            st.session_state.questions[i]["type"] = st.selectbox("Type", ["text", "number", "yes-no"], key=f"qtype_{i}")

        if st.button("Start Form"):
            st.session_state.answers = [None for _ in st.session_state.questions]
            st.session_state.step = "fill"

        st.markdown('</div>', unsafe_allow_html=True)

# ------------------ STEP: FILL ------------------
elif st.session_state.step == "fill":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-subtitle">Please fill the form below:</div>', unsafe_allow_html=True)

        for i, q in enumerate(st.session_state.questions):
            if q["type"] == "text":
                st.session_state.answers[i] = st.text_input(q["text"], key=f"ans_text_{i}")
            elif q["type"] == "number":
                st.session_state.answers[i] = st.number_input(q["text"], key=f"ans_num_{i}")
            elif q["type"] == "yes-no":
                st.session_state.answers[i] = st.radio(q["text"], ["yes", "no"], key=f"ans_yn_{i}")

        if st.button("Submit"):
            st.session_state.step = "summary"

        st.markdown('</div>', unsafe_allow_html=True)

# ------------------ STEP: SUMMARY ------------------
elif st.session_state.step == "summary":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">📊 Summary: {st.session_state.title}</div>', unsafe_allow_html=True)

        results = []
        for i, q in enumerate(st.session_state.questions):
            st.write(f"**{i+1}. {q['text']}** → {st.session_state.answers[i]} ({q['type']})")
            results.append({
                "Question": q["text"],
                "Type": q["type"],
                "Answer": st.session_state.answers[i]
            })

        df = pd.DataFrame(results)

        st.download_button(
            label="⬇️ Download CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"quorix_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

        txt_export = f"Form Title: {st.session_state.title}\n\n"
        for i, q in enumerate(st.session_state.questions):
            txt_export += f"{i+1}. {q['text']} → {st.session_state.answers[i]} ({q['type']})\n"

        st.download_button(
            label="📝 Download TXT",
            data=txt_export,
            file_name=f"quorix_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

        if st.button("🌀 Create Another Form"):
            st.session_state.step = "setup"
            st.session_state.title = ""
            st.session_state.questions = []
            st.session_state.answers = []
            st.session_state.num_questions = 1

        st.markdown('</div>', unsafe_allow_html=True)

