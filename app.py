import streamlit as st
from crew import run_crew

# Streamlit UI
st.title("AI Collaborative Research and Writing Platform")

# Input for the topic
topic = st.text_input("Enter the topic:")

# Button to start the conversation
if st.button("Start"):
    if topic:
        with st.spinner('Running the agents...'):
            # Run the crew and get the result
            result = run_crew(topic)
        
        # Display the results
        st.subheader("Conversation and Results")
        st.write(result)
    else:
        st.error("Please enter a topic.")
