import streamlit as st
import pyautogui
import time

def emergency_ui():
    st.header("🚨 Emergency SOS ")
    st.write("allows users to quickly and easily alert emergency services or designated contacts in a crisis, providing a quick way to request help. ")
    
    if "sos_triggered" not in st.session_state:
        st.session_state.sos_triggered = False
    if "details_submitted" not in st.session_state:
        st.session_state.details_submitted = False
    if "auto_name" not in st.session_state:
        st.session_state.auto_name = ""
    if "auto_location" not in st.session_state:
        st.session_state.auto_location = ""
    if "typing_step" not in st.session_state:
        st.session_state.typing_step = 0

    if not st.session_state.sos_triggered:
        if st.button("🔴 SOS"):
            st.session_state.sos_triggered = True
            st.rerun()

    elif not st.session_state.details_submitted:
        st.success("✅ Auto-filling your details...")
        
        name = "Nirbhaya Sharma"
        location = "Ahmedabad, Gujarat"
        
        st.text_input("Name", value=st.session_state.auto_name, disabled=True, key="name_display")
        st.text_input("Location", value=st.session_state.auto_location, disabled=True, key="location_display")

        if st.session_state.typing_step < len(name):
            st.session_state.auto_name += name[st.session_state.typing_step]
            st.session_state.typing_step += 1
            time.sleep(0.1)
            st.rerun()
        elif st.session_state.typing_step < len(name) + len(location):
            index = st.session_state.typing_step - len(name)
            st.session_state.auto_location += location[index]
            st.session_state.typing_step += 1
            time.sleep(0.1)
            st.rerun()
        else:
            st.info("Auto-submitting ...")
            time.sleep(1)
            
            pyautogui.press('enter')
            st.session_state.details_submitted = True
            st.rerun()

    else:
        st.success("🚨 SOS Sent Successfully!")
        st.write(f"**Name:** {st.session_state.auto_name}")
        st.write(f"**Location:** {st.session_state.auto_location}")

        

