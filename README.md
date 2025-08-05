# 🗣️ AI Voice Assistant with LangChain + Ollama

A simple voice assistant that listens to your speech, converts it to text, queries a local LLM using LangChain, and speaks the response back using TTS.

---

## 🎯 Features

- 🎤 Speech-to-text using `SpeechRecognition` + microphone
- 🤖 Local LLM querying via `langchain-ollama` (Mistral model)
- 🧠 Maintains chat history using LangChain memory
- 🔊 Text-to-speech using `pyttsx3`
- 🖥️ UI powered by Streamlit

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/AzkaSahar/AI-Voice-Assistant.git
cd AI-Voice-Assistant
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ You may need to install `pyaudio` manually:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🚀 Usage

### 1. Start Ollama (if not already running)

Make sure Ollama is installed and the `mistral` model is available:

```bash
ollama run mistral
```

### 2. Run the Streamlit app

```bash
streamlit run ai_voice_Assistant.py
```
---

## 🧠 How It Works

* Listens to user voice input
* Transcribes using `SpeechRecognition`
* Passes query and history to LangChain-powered Mistral model via `langchain-ollama`
* Speaks response using `pyttsx3`
* Maintains a visible chat history

---

## 📝 License

MIT – Free to use, modify, and share.

