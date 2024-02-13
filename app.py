import streamlit as st
from streamlit_chat import message
import requests
import asyncio

API_CHATBOT = "http://localhost:5002/smi/chatbot"

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

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")

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
    
    st.button("Clear message", on_click=on_clear_btn_click)
