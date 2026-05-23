import os
import tempfile
import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

LANG_OPTIONS = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
}

VOICE_OPTIONS = {
    "English (US) - JennyNeural": "en-US-JennyNeural",
    "English (US) - GuyNeural": "en-US-GuyNeural",
    "English (UK) - LibbyNeural": "en-GB-LibbyNeural",
    "English (AU) - HayleyNeural": "en-AU-HayleyNeural",
    "French (France) - AriaNeural": "fr-FR-AriaNeural",
    "Spanish (Spain) - ElviraNeural": "es-ES-ElviraNeural",
    "German (Germany) - KatjaNeural": "de-DE-KatjaNeural",
}

st.set_page_config(page_title="Azure Text-to-Speech Reader", page_icon="🔊", layout="centered")

st.title("gTTS Text-to-Speech Reader")
st.markdown(
    "Enter your text below, choose a translation language if needed, and gTTS will generate audio for playback in the browser."
)

text_to_read = st.text_area("Text to speak", value="Hello, I am reading this text out loud using gTTS.")

translate_enabled = st.checkbox("Translate before speaking?")
if translate_enabled:
    target_lang_label = st.selectbox("Target language", list(LANG_OPTIONS.keys()))
    target_lang = LANG_OPTIONS[target_lang_label]
else:
    target_lang = None

if st.button("Read text aloud"):
    if not text_to_read.strip():
        st.error("Please enter some text to read.")
        st.stop()

    try:
        # perform translation if requested
        final_text = text_to_read
        if target_lang:
            try:
                translator = GoogleTranslator(source="auto", target=target_lang)
                final_text = translator.translate(text_to_read)
                st.info(f"Translated ({target_lang_label}): {final_text}")
            except Exception as texc:
                st.warning(f"Translation failed, proceeding with original text: {texc}")

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
            audio_filename = temp_audio.name

        # choose gTTS language based on translation, else default to English
        gtts_lang = target_lang if target_lang else "en"
        tts = gTTS(text=final_text, lang=gtts_lang)
        tts.save(audio_filename)
        with open(audio_filename, "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.success("Audio generated with gTTS")
        st.audio(audio_bytes, format="audio/mp3")
        st.download_button("Download audio (.mp3)", data=audio_bytes, file_name="speech.mp3", mime="audio/mpeg")
    except Exception as exc:
        st.error(f"Error generating speech: {exc}")

st.markdown("---")
st.markdown(
    "**Notes:**\n- This app uses gTTS only, so no Azure API key is required.\n- Translation is optional; if selected, gTTS will speak in the target language.\n- If audio does not play, download the MP3 file and play locally."
)
