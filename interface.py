
# ✅ app.py (Streamlit interface)
import streamlit as st
from auth import login_page
from Crewkickoff import run_ai_workflow
from database import log_interaction

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()

st.title("🧠 AI Research Assistant")
topic = st.text_input("Enter your AI research topic:")
if st.button("Run Research") and topic:
    with st.spinner("Agents are thinking..."):
        result = run_ai_workflow({"topic": topic})
        log_interaction(st.session_state.user_id, topic, result)
        st.session_state.result = result

if "result" in st.session_state:
    st.subheader("📝 Final Report")
    st.markdown(st.session_state.result)
    st.download_button("Download Markdown", st.session_state.result, file_name="report.md")
