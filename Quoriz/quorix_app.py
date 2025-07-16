import streamlit as st
import pandas as pd
import datetime

# -----------------------------------
# CONFIG
# -----------------------------------
st.set_page_config(page_title="Quorix", layout="centered")

st.markdown("""
    <style>
    body { background-color: #f5f5f5; }
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
        .form-card {
            padding: 15px;
        }
        .form-title {
            font-size: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# STATE INIT
# -----------------------------------
if "phase" not in st.session_state:
    st.session_state.phase = "setup"
    st.session_state.questions = []
    st.session_state.title = ""
    st.session_state.responses = []

# -----------------------------------
# SETUP PHASE
# -----------------------------------
if st.session_state.phase == "setup":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-title">🧠 Quorix - Create Your Form</div>', unsafe_allow_html=True)
        st.session_state.title = st.text_input("Form Title")
        num = st.number_input("How many questions?", min_value=1, max_value=10, step=1)

        if st.button("Next"):
            st.session_state.questions = [{"text": "", "type": "text", "answer": None} for _ in range(num)]
            st.session_state.phase = "build"
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# BUILD PHASE
# -----------------------------------
elif st.session_state.phase == "build":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-subtitle">Enter your questions and types:</div>', unsafe_allow_html=True)

        for i, q in enumerate(st.session_state.questions):
            q["text"] = st.text_input(f"Q{i+1}", key=f"qtext_{i}")
            q["type"] = st.selectbox("Type", ["text", "number", "yes-no"], key=f"qtype_{i}")

        if st.button("Start Form"):
            st.session_state.phase = "fill"
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# FILL PHASE
# -----------------------------------
elif st.session_state.phase == "fill":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">{st.session_state.title}</div>', unsafe_allow_html=True)

        for i, q in enumerate(st.session_state.questions):
            if q["type"] == "text":
                q["answer"] = st.text_input(q["text"], key=f"ans_text_{i}")
            elif q["type"] == "number":
                q["answer"] = st.number_input(q["text"], key=f"ans_num_{i}")
            elif q["type"] == "yes-no":
                q["answer"] = st.radio(q["text"], ["yes", "no"], key=f"ans_yn_{i}")

        if st.button("Submit"):
            st.session_state.phase = "summary"
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# SUMMARY PHASE
# -----------------------------------
elif st.session_state.phase == "summary":
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="form-title">📊 Summary: {st.session_state.title}</div>', unsafe_allow_html=True)

        data = []
        for i, q in enumerate(st.session_state.questions):
            st.write(f"**{i+1}. {q['text']}** → {q['answer']} ({q['type']})")
            data.append({"Question": q["text"], "Type": q["type"], "Answer": q["answer"]})

        df = pd.DataFrame(data)

        st.download_button(
            label="⬇️ Download as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"quorix_response_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

        text_export = f"Form Title: {st.session_state.title}\n\n"
        for i, q in enumerate(st.session_state.questions):
            text_export += f"{i+1}. {q['text']} → {q['answer']} ({q['type']})\n"

        st.download_button(
            label="📝 Download as TXT",
            data=text_export,
            file_name=f"quorix_summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

        if st.button("🌀 Create New Form"):
            st.session_state.phase = "setup"
            st.session_state.questions = []
            st.session_state.title = ""
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)
