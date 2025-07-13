import streamlit as st

st.title("🕓 Your Prompt History")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("🧹 Clear history"):
    st.session_state.history = []

if st.session_state.history:
    for i, entry in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{i}.** `{entry}`")
else:
    st.info("No prompt history yet.")
