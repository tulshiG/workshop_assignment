import streamlit as st
from chatbot_B import chatbot_ui
from emergency_C import emergency_ui

# Page settings
st.set_page_config(page_title="NirbhayaConnect", layout='wide')
st.title('NirbhayaConnect - Your Safety Companion')

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
with st.sidebar:
    st.title("🔒 NirbhayaConnect")
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📋 How We Help"):
        st.session_state.page = "Help"
    if st.button("🤖 Chat with Safety Bot"):
        st.session_state.page = "Chatbot"
    if st.button("🚨 Emergency Help"):
        st.session_state.page = "Emergency"

# Main content rendering
if st.session_state.page == "Home":
    st.header("Welcome to NirbhayaConnect")
    st.write("Empowering women with instant help, safety tips, and emergency support.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚨 Emergency Help", key="home_emergency"):
            st.session_state.page = "Emergency"
    with col2:
        if st.button("🤖 Chat with Safety Bot", key="home_chatbot"):
            st.session_state.page = "Chatbot"

elif st.session_state.page == "Help":
    st.header("How NirbhayaConnect Supports You:")
    st.markdown("""
    - 🧠 24/7 Smart Safety Chatbot  
    - 🚨 One-click Emergency Alert System  
    - 📍 Real-time Location Sharing with Police  
    - 📋 Safety Tips & Emergency Numbers  
    """)

elif st.session_state.page == "Chatbot":
    chatbot_ui()

elif st.session_state.page == "Emergency":
    emergency_ui()
