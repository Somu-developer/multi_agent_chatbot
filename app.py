import streamlit as st
from mcp import handle_message
from memory import load_memory

st.set_page_config(page_title="Multi Agent Chatbot AI", page_icon="💬")
st.title("💬 Multi Agent Chatbot AI(Free)")
USER_ID = "demo_user"
if "messages" not in st.session_state:
    st.session_state.messages = []

# show past from all bots
mem = load_memory()
user_mem = mem.get(USER_ID, {})

with st.expander("Stored conversations (all_bots)", expanded=False):
    st.json(user_mem)

user_input = st.text_input("Type your message:")

if st.button("Send") and user_input.strip():
    bot_used, reply = handle_message(USER_ID, user_input.strip())
    st.session_state.messages.append(("you", user_input.strip(), bot_used))
    st.session_state.messages.append((bot_used, reply, bot_used))

#display chat

for role, text, bot_name in st.session_state.messages:
    if role == "you":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**{bot_name} Bot:** {text}")
