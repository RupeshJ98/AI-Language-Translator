# AI-Language-Translator
📌 Project Title
AI-Powered Language Translator & Learning Assistant

# 🔍 Problem Statement
Real-time translation apps exist, but most are focused only on basic input/output. This app simulates a smart voice assistant that not only translates, but also helps the user learn the target language.

# 🧠 Key Features
-Real-time voice input & transcription

-Multilingual translation with Google Translate

-Text-to-speech playback using gTTS

-Word-by-word learning mode

-Pronunciation display

-Fully built in Python with Streamlit

# 🛠️ Tech Stack
-Python, Streamlit

-speech_recognition, googletrans, gTTS, base64

-Fallbacks handled with error catching

-(Optional) Whisper, TTS, or DB for extended versions

# 💡 Lessons Learned
-Working with APIs for voice and translation

-Structuring an interactive Streamlit app

-Managing session state and dynamic UI updates

-Handling multilingual text and user-friendly design

# 🚀 Future Improvements
-Flashcard-style vocab quizzes

-Offline support with Whisper and local TTS

-Saving vocab list as CSV or PDF

-Multiple speaker modes (interpreter style)

-Deployment via Streamlit Cloud or Hugging Face Spaces

# How to Run
```bash
git clone https://github.com/RupeshJ98/AI-Language-Translator.git
cd AI-Language-Translator
pip install -r requirements.txt
streamlit run app.py
