import os
import streamlit as st

st.set_page_config(page_title="Add Two Numbers", layout="centered")

st.title("✅ Minimal Streamlit + Docker + Hugging Face")
st.write("Enter two numbers and click **Add**.")

a = st.number_input("A", value=1.0)
b = st.number_input("B", value=2.0)

if st.button("Add"):
    st.success(f"Result: {a + b}")

st.divider()
st.subheader("Token check (optional, but proves secrets work)")

if st.button("Who am I (Hugging Face)?"):
    token = os.getenv("HF_TOKEN")
    if not token:
        st.error("HF_TOKEN is not set in the container environment.")
    else:
        try:
            from huggingface_hub import whoami
            info = whoami(token=token)
            st.success(f"Authenticated as: {info.get('name')}")
        except Exception as e:
            st.error(f"Token check failed: {e}")
