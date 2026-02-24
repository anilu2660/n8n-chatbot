import streamlit as st
import requests


st.title("🤝 Your Personal Assistant")

st.subheader("What can your personal assistant do?")


st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)


st.subheader("💬 Chat with your assistant")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_message = st.chat_input()

      

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
       
        st.session_state.messages.append({"role": "user", "content": user_message})
    
  
    try:
        response = requests.post(
            "https://anujup.app.n8n.cloud/webhook/684437fb-9068-4801-ad25-e2918697b22d",  # production n8n webhook URL
            json={"message": user_message}
        )
        
        if response.status_code != 200:
            ai_response = f"⚠️ Webhook returned status {response.status_code}. Make sure your n8n workflow is **activated**."
        elif not response.text.strip():
            ai_response = "⚠️ Webhook returned an empty response. Make sure your n8n workflow is **activated** and the webhook node is set to **'Respond to Webhook'**."
        else:
           
            result = response.json()
            
           
            if isinstance(result, list):
                ai_response = result[0]["output"]
            elif isinstance(result, dict):
                ai_response = result.get("output", str(result))
            else:
                ai_response = str(result)
    except requests.exceptions.ConnectionError:
        ai_response = "⚠️ Could not connect to the n8n webhook. Please check your internet connection and webhook URL."
    except Exception as e:
        ai_response = f"⚠️ Error: {str(e)}"
    
    
    with st.chat_message("assistant"):
        st.markdown(ai_response)
       
        st.session_state.messages.append({"role": "assistant", "content": ai_response})