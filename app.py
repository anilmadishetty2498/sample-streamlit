# Databricks notebook source
import streamlit as st

# Title of the app
st.title("Quick Streamlit App")

# Text input
user_input = st.text_input("Enter something:")

# Button
if st.button("Submit"):
    if user_input:
        st.write(f"You entered: {user_input}")
    else:
        st.write("Please enter some text.")