import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from backEnd import chatbot

thread_id='1'
config = {'configurable': {'thread_id': thread_id}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    if message['role'] == 'user':
        with st.chat_message('user'):
            st.write(message['content'])
    else:
        with st.chat_message('assistant'):
            st.write(message['content'])
    
user_input = st.chat_input('type here ')    

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.write(user_input)
    
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= config,
                stream_mode= 'messages'
            )
        )
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})    