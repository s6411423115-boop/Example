import streamlit as st
st.title("quot;My First Streamlit App&quot")
name = st.text_input("quot;Enter your name&quot")

b = st.button("click Me")
if b:
 st.write(f"Hello, {name}!")
