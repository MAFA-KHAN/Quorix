import streamlit as st
import pandas as pd
import datetime

# ------------------ CONFIG & CSS ------------------
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

# ------------------ SAFE RERUN HANDLING ------------------
if "refresh" in st.session_state and st.session_state.refresh:
    st.session_state.refresh = False
    st.experimental_rerun()

# ------------------ SESSION INIT ------------------
if "step" not in st.session_state:
    st.session_state.step = "setup"
    st.session_state.title = ""
    st.session_state.questions = []
    st.session_state.answers = []

# ------------------ SETUP STEP ------------------
if st.session_state.step == "setup":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-title">🧠 Quorix - Create Your Form</div>', unsafe_allow_html=True)

        title = st.text_input("Enter your form title")
        num = st.number_input("How many questions?", min_value=1, max_value=10, step=1)
        next_btn = st.button("Next")
        st.markdown('</div>', unsafe_allow_html=True)

    if next_btn and title:
        st.session_state.title = title
        st.session_state.questions = [{"text": "", "type": "text"} for _ in range(num)]
        st.session_state.step = "build"
        st.session_state.refresh = True

# ------------------ BUILD STEP ------------------
elif st.session_state.step == "build":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-subtitle">Write your questions and choose types:</div>', unsafe_allow_html=True)

        for i, q in enumerate(st.session_state.questions):
            q["text"] = st.text_input(f"Q{i+1}", key=f"qtext_{i}")
            q["type"] = st.selectbox("Type", ["text", "number", "yes-no"], key=f"qtype_{i}")

        start_form = st.button("Start Form")
        st.markdown('</div>', unsafe_allow_html=True)

    if start_form:
        st.session_state.answers = [None for _ in st.session_state.questions]
        st.session_state.step = "fill"
        st.session_state.refresh = True

# ------------------ FILL STEP ------------------
elif st.session_state.step == "fill":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-subtitle">Please fill the form:</div>', unsafe_allow_html=True)

        for i, q in enumerate(st.session_state.questions):
            if q["type"] == "text":
                st.session_state.answers[i] = st.text_input(q["text"], key=f"ans_text_{i}")
            elif q["type"] == "number":
                st.session_state.answers[i] = st.number_input(q["text"], key=f"ans_num_{i}")
            elif q["type"] == "yes-no":
                st.session_state.answers[i] = st.radio(q["text"], ["yes", "no"], key=f"ans_yn_{i}")

        submit = st.button("Submit")
        st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        st.session_state.step = "summary"
        st.session_state.refresh = True

# ------------------ SUMMARY STEP ------------------
elif st.session_state.step == "summary":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">📊 Summary: {st.session_state.title}</div>', unsafe_allow_html=True)

        data = []
        for i, q in enumerate(st.session_state.questions):
            st.write(f"**{i+1}. {q['text']}** → {st.session_state.answers[i]} ({q['type']})")
            data.append({
                "Question": q["text"],
                "Type": q["type"],
                "Answer": st.session_state.answers[i]
            })

        df = pd.DataFrame(data)

        st.download_button(
            label="⬇️ Download as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"quorix_response_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

        txt = f"Form Title: {st.session_state.title}\n\n"
        for i, q in enumerate(st.session_state.questions):
            txt += f"{i+1}. {q['text']} → {st.session_state.answers[i]} ({q['type']})\n"

        st.download_button(
            label="📝 Download as TXT",
            data=txt,
            file_name=f"quorix_summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

        reset_btn = st.button("🌀 Create Another Form")
        st.markdown('</div>', unsafe_allow_html=True)

    if reset_btn:
        st.session_state.step = "setup"
        st.session_state.questions = []
        st.session_state.answers = []
        st.session_state.title = ""
        st.session_state.refresh = True

