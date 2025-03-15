import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# --- Use a valid model ---
MODEL_NAME = "gpt2"  # Replace with another HF model if needed

# --- Load model with caching ---
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

# --- Generate bot response ---
def generate_response(prompt):
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=100,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# --- Predefined Safety Prompts ---
safety_prompts = [
    "How can I stay safe when walking alone at night?",
    "What should I do if I'm being followed?",
    "Give me emergency contact numbers in my area.",
    "How do I report harassment?",
    "What to do if I feel unsafe in a cab?",
]

# --- Chatbot UI ---
def chatbot_ui():
    st.header("Safety Bot - Ask Anything")
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # --- Suggestion Buttons (Moved to Top) ---
    st.markdown("💡 **Safety Suggestions:**")
    cols = st.columns(2)
    for i, prompt in enumerate(safety_prompts):
        cols[i % 2].button(prompt, on_click=lambda p=prompt: set_user_input(p))

    st.markdown("---")  # Divider

    # --- Input & Send Button Side-by-Side ---
    input_col, button_col = st.columns([5, 1])
    with input_col:
        st.text_input("Ask me anything about your safety 👇", key="user_input", label_visibility="collapsed",placeholder="Type your question here...")
    with button_col:
        st.write("")  # For alignment
        st.button("Send", on_click=handle_user_input)

    # --- Display Chat History ---
    for sender, msg in st.session_state["messages"]:
        st.markdown(f"**{sender}:** {msg}")

# --- Input Handlers ---
def set_user_input(prompt):
    st.session_state["user_input"] = prompt

def handle_user_input():
    user_input = st.session_state["user_input"]
    if user_input.strip():
        st.session_state["messages"].append(("User", user_input))
        response = generate_response(user_input)
        st.session_state["messages"].append(("Bot", response))
        st.session_state["user_input"] = ""

# --- Run UI ---
chatbot_ui()
