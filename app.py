import streamlit as st
st.title("quot;My First Streamlit App&quot")
name = st.text_input("quot;Enter your name&quot")
if name:
 st.write(f"quot;Hello, {name}!")
