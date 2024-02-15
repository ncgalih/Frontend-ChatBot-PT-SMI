import streamlit as st
from streamlit_chat import message
import requests
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

API_CHATBOT = os.getenv('API_CHATBOT')

async def get_response(question):
    response = requests.get(API_CHATBOT, params={'query': question})
    return response.json()["message"]["content"]

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with st.spinner("Generating response"):
        response = loop.run_until_complete(get_response(user_input))
        st.session_state.generated.append({'data': response})
    st.session_state.user_input = ""

def on_clear_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

st.session_state.setdefault(
    'past', []
)
st.session_state.setdefault(
    'generated', []
)

st.title("SMIBot")

chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True
        )

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
    st.button("Clear message", on_click=on_clear_btn_click)