import streamlit as st
from chatbot.chatbot_interface import main  # Assuming your chatbot logic is inside this function

def app():
    # Title of the app
    st.title("MAS Chatbot App")

    # Text input for the user to enter their query
    user_query = st.text_input("Enter your query:")

    # When the user presses 'Enter', process the query
    if user_query:
        # Call the main chatbot function to process the query
        st.write(f"Query: {user_query}")  # Display the query
        response = main(user_query)  # Assuming `main` can handle the query
        st.write(f"Response: {response}")  # Display the response from the chatbot

if __name__ == "__main__":
    app()
