import streamlit as st
from chatbot.chatbot_interface import main  # Import the main function from chatbot interface
import spacy

try:
    # Try to load the spaCy model
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    # Catch any exception (e.g., if the model isn't found) and raise it
    raise RuntimeError(f"Error loading spaCy model: {str(e)}. Please make sure the model is included in the requirements.")

def app():
    # Title of the app
    st.title("MAS Chatbot App")

    # Text input for the user to enter their query
    user_query = st.text_input("Enter your query:")

    # When the user presses 'Enter', process the query
    if user_query:
        st.write(f"Query: {user_query}")  # Display the query
        response = main(user_query)  # Call the main function with the query
        st.write(f"Response: {response}")  # Display the response from the chatbot

if __name__ == "__main__":
    app()
