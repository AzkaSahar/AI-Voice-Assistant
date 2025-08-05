import speech_recognition as sr
import pyttsx3 
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st

llm=OllamaLLM(model="mistral")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=ChatMessageHistory()
engine=pyttsx3.init()
engine.setProperty("rate",160)
recognizer=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        st.write("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
    try:
        query=recognizer.recognize_google(audio)
        st.write(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        st.write("Sorry couldn't understand, please repeat")
        return ""
    except sr.RequestError:
        st.write("Speech service unavailable")
        return ""

prompt=PromptTemplate(input_variables=["chat_history","question"], template="Previous conversation:{chat_history}\nUser: {question}\nAI: ")
def run_chain(question):
    chat_history_text="\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])
    response=llm.invoke(prompt.format(chat_history=chat_history_text,question=question))
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response

st.title("AI Voice Assisstant")
st.write("Click button to speak")

if st.button("Start Listening"):
    user_query=listen()
    if user_query:
        response=run_chain(user_query)
        st.write(f"**You:** {user_query}")
        st.write(f"**AI:** {response}")
        speak(response)

st.subheader("Chat history")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")

