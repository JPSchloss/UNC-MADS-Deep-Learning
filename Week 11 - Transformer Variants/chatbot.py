import streamlit as st
from openai import OpenAI

# Set up OpenAI client
client = OpenAI(api_key=api_key)  # Replace with your OpenAI API key

# Streamlit UI
st.title("💬 OpenAI Chatbot")
st.write("A simple chatbot powered by OpenAI.")

# Ensure session state is initialized
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history using Streamlit's `st.chat_message`
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Add user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Display user message in chat interface
    with st.chat_message("user"):
        st.write(user_input)

    # Show a loading indicator while waiting for OpenAI's response
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state["messages"]
        )

    # Get AI response
    ai_response = response.choices[0].message.content

    # Add AI response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": ai_response})

    # Display AI response in chat interface
    with st.chat_message("assistant"):
        st.write(ai_response)
