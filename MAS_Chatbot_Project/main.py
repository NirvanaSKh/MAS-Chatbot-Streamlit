import streamlit as st
from chatbot.chatbot_interface import main  # Assuming you have a `main` function in `chatbot/chatbot_interface.py`

def app():
    st.title("MAS Chatbot App")
    main()  # Call the function that starts your chatbot interface

if __name__ == "__main__":
    app()
