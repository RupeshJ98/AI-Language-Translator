import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile
import os
import base64

from datetime import datetime

st.set_page_config(page_title="Real-Time AI Translator", layout="centered")
st.title("🎧 AI Language Translator – Chat Style")

# --- Init session state ---
if "history" not in st.session_state:
    st.session_state.history = []

if "vocab_list" not in st.session_state:
    st.session_state.vocab_list = []

# --- Sidebar: Settings ---
st.sidebar.markdown("### 🌐 Language Settings")
input_lang = st.sidebar.selectbox("🎙️ Input language:", ["en", "hi", "es", "fr", "de","te"])
output_lang = st.sidebar.selectbox("🔊 Output language:", ["en", "hi", "es", "fr", "de","te"])

st.sidebar.markdown("### 🧠 Learning Mode")
learning_mode = st.sidebar.checkbox("Enable word-by-word breakdown")

st.markdown("### 🎤 Click to start speaking")

if st.button("🎙️ Speak Now"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=input_lang)
        st.success(f"✅ You said: {text}")

        translator = Translator()
        translated = translator.translate(text, src=input_lang, dest=output_lang).text

        # Text-to-Speech
        tts = gTTS(text=translated, lang=output_lang)
        temp_path = tempfile.mktemp(suffix=".mp3")
        tts.save(temp_path)

# Save to chat history
        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "input": text,
            "translated": translated,
            "audio": temp_path
})

# Auto-play audio
        with open(temp_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            b64 = base64.b64encode(audio_bytes).decode()
            st.markdown(f"""
                <audio autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """, unsafe_allow_html=True)

        

        # ✅ Move this block inside
        if learning_mode:
            st.markdown("### 🔍 Word-by-Word Breakdown")
        words = text.split()
        for word in words:
            try:
                translation_result = translator.translate(word, src=input_lang, dest=output_lang)
                word_translation = translation_result.text
                pronunciation = translation_result.pronunciation or "N/A"

                #   Show word info
                col1, col2, col3 = st.columns([3, 3, 1])
                col1.markdown(f"**{word}** → *{word_translation}*")
                col2.markdown(f"_Pronunciation_: `{pronunciation}`")

                # Save to vocab list button
                if col3.button("📌", key=f"save_{word}"):
                    st.session_state.vocab_list.append({
                        "word": word,
                        "translation": word_translation,
                        "pronunciation": pronunciation
                    })

            except:
                st.markdown(f"**{word}** → *(unavailable)*")


    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

if st.session_state.vocab_list:
    st.markdown("## 📚 Saved Vocabulary")
    for item in st.session_state.vocab_list:
        st.markdown(f"- **{item['word']}** → *{item['translation']}* (`{item['pronunciation']}`)")


# --- Display chat history ---
if st.session_state.history:
    st.markdown("### 💬 Translation Chat History")
    for entry in reversed(st.session_state.history):
        with st.expander(f"🕒 {entry['time']} | You said: {entry['input']}"):
            st.markdown(f"**Translated:** {entry['translated']}")
            st.audio(entry["audio"], format="audio/mp3")
