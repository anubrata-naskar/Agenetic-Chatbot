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
        
    chatbot_response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=config)   
    ai_message = chatbot_response['messages'][-1] 

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message.content})
    with st.chat_message('assistant'):
        st.write(ai_message.content)
        