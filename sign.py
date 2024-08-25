import streamlit as st
import time

# Display a message indicating buffering
st.title("Buffering...")
st.write("Please wait while we process your request.")

# Buffer forever by running an infinite loop
while True:
    with st.spinner("Processing..."):
        time.sleep(1)  # Simulate processing time with a delay
