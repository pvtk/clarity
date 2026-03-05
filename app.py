import streamlit as st
from openai import OpenAI

# 1. Setup - Securely get your API Key
# In a real app, you'd use st.secrets for safety!
client = OpenAI(api_key="CLARITYSECRET")

st.title("✍️ The Clarity Engine")

user_input = st.text_area("Vague Text:", placeholder="e.g., Send me that stuff when you can.")
tone_choice = st.selectbox("Preserve Tone:", ["Professional", "Casual", "Academic"])

if st.button("Clarify"):
    if user_input:
        # 2. Crafting the "Brain" Instructions
        system_instruction = f"""
        You are a text disambiguation expert. 
        Your task: Rewrite the user's text to remove vague pronouns and indefinite timeframes.
        CRITICAL: You MUST keep the tone exactly as '{tone_choice}'. 
        If you are unsure of a term, provide the most likely clarification.
        """

        # 3. Call the AI
        response = client.chat.completions.create(
            model="gpt-4o-mini", # High speed, low cost for prototypes
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3 # Low temperature = more focus, less "wandering"
        )

        # 4. Show the result
        refined_text = response.choices[0].message.content
        st.subheader("Clarified Result:")
        st.write(refined_text)
    else:
        st.error("Please enter text to clarify.")
