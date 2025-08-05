import streamlit as st
import json
import os
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from backEnd import chatbot


CONVERSATIONS_FILE = "conversations.json"

def load_conversations():
    if os.path.exists(CONVERSATIONS_FILE):
        try:
            with open(CONVERSATIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading conversations: {e}")
            return {}
    return {}


def save_conversations(conversations):
    try:
        with open(CONVERSATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Error saving conversations: {e}")


def create_new_conversation():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    conversation_id = f"chat_{timestamp}"
    return conversation_id

def get_conversation_title(messages):
    
    if messages and len(messages) > 0:
        first_message = messages[0]['content']
        title = first_message[:50].strip()
        if len(first_message) > 50:
            title += "..."
        return title
    return "New Chat"


if 'conversations' not in st.session_state:
    st.session_state.conversations = load_conversations()

if 'current_conversation_id' not in st.session_state:
    st.session_state.current_conversation_id = None

if 'message_history' not in st.session_state:
    st.session_state.message_history = []


st.set_page_config(page_title="AI Chatbot", layout="wide")

with st.sidebar:
    st.title("💬 Chat History")
    
    if st.button("➕ New Chat", use_container_width=True):
        if st.session_state.current_conversation_id and st.session_state.message_history:
            st.session_state.conversations[st.session_state.current_conversation_id] = {
                'messages': st.session_state.message_history,
                'timestamp': datetime.now().isoformat(),
                'title': get_conversation_title(st.session_state.message_history)
            }
            save_conversations(st.session_state.conversations)
        
        st.session_state.current_conversation_id = create_new_conversation()
        st.session_state.message_history = []
        st.rerun()
    
    st.divider()
    

    if st.session_state.conversations:
        st.subheader("Previous Conversations")
        
        sorted_conversations = sorted(
            st.session_state.conversations.items(),
            key=lambda x: x[1].get('timestamp', ''),
            reverse=True
        )
        
        for conv_id, conv_data in sorted_conversations:
            title = conv_data.get('title', 'Untitled Chat')
            timestamp = conv_data.get('timestamp', '')
            
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime("%m/%d %H:%M")
                except:
                    time_str = ""
            else:
                time_str = ""
            
            button_label = f"💬 {title}"
            if time_str:
                button_label += f"\n🕒 {time_str}"
            
            if st.button(button_label, key=f"conv_{conv_id}", use_container_width=True):
                if st.session_state.current_conversation_id and st.session_state.message_history:
                    st.session_state.conversations[st.session_state.current_conversation_id] = {
                        'messages': st.session_state.message_history,
                        'timestamp': datetime.now().isoformat(),
                        'title': get_conversation_title(st.session_state.message_history)
                    }
                    save_conversations(st.session_state.conversations)
                
                st.session_state.current_conversation_id = conv_id
                st.session_state.message_history = conv_data.get('messages', [])
                st.rerun()
  
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button("🗑️", key=f"del_{conv_id}", help="Delete conversation"):
                    if conv_id in st.session_state.conversations:
                        del st.session_state.conversations[conv_id]
                        save_conversations(st.session_state.conversations)
                        if st.session_state.current_conversation_id == conv_id:
                            st.session_state.current_conversation_id = create_new_conversation()
                            st.session_state.message_history = []
                        st.rerun()
    else:
        st.write("No conversations yet. Start chatting!")

st.title("🤖 AI Chatbot")


if not st.session_state.current_conversation_id:
    st.session_state.current_conversation_id = create_new_conversation()


if st.session_state.message_history:
    current_title = get_conversation_title(st.session_state.message_history)
    st.caption(f"Current chat: {current_title}")


for message in st.session_state.message_history:
    if message['role'] == 'user':
        with st.chat_message('user'):
            st.write(message['content'])
    else:
        with st.chat_message('assistant'):
            st.write(message['content'])


user_input = st.chat_input('Type your message here...')

if user_input:
    config = {'configurable': {'thread_id': st.session_state.current_conversation_id}}
    
    st.session_state.message_history.append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.write(user_input)

    try:
        with st.chat_message('assistant'):
            with st.spinner('Thinking...'):
                chatbot_response = chatbot.invoke(
                    {'messages': [HumanMessage(content=user_input)]}, 
                    config=config
                )
                ai_message = chatbot_response['messages'][-1]
                st.write(ai_message.content)
        

        st.session_state.message_history.append({'role': 'assistant', 'content': ai_message.content})
        
 
        st.session_state.conversations[st.session_state.current_conversation_id] = {
            'messages': st.session_state.message_history,
            'timestamp': datetime.now().isoformat(),
            'title': get_conversation_title(st.session_state.message_history)
        }
        save_conversations(st.session_state.conversations)
        
    except Exception as e:
        st.error(f"Error getting AI response: {e}")
        