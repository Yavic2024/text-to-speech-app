from dotenv import load_dotenv
import streamlit as st
import asyncio
import edge_tts
import tempfile
import os
import PyPDF2
from pathlib import Path

# Load environment variables
load_dotenv()

# Language configuration
LANGUAGES = {
    "English (US)": {
        "voices": ["en-US-AriaNeural", "en-US-GuyNeural"],
        "sample": "Hello! Welcome to the Text to Speech app."
    },
    "English (UK)": {
        "voices": ["en-GB-LibbyNeural", "en-GB-RyanNeural"],
        "sample": "Hello! Welcome to the Text to Speech app."
    },
    "Hindi": {
        "voices": ["hi-IN-SwaraNeural", "hi-IN-MadhurNeural"],
        "sample": "नमस्ते! टेक्स्ट टू स्पीच ऐप में आपका स्वागत है।"
    },
    "Spanish": {
        "voices": ["es-ES-ElviraNeural", "es-ES-AlvaroNeural"],
        "sample": "¡Hola! Bienvenido a la aplicación de texto a voz."
    }
}

# Initialize session state
for key in ["theme", "text", "history", "last_audio"]:
    if key not in st.session_state:
        st.session_state[key] = "" if key == "text" else []

# Theme configuration
def set_theme():
    if st.session_state.theme == "dark":
        st.markdown("""
            <style>
            body { background-color: #222; color: #eee; }
            .stTextInput>div>div>input, .stTextArea>div>textarea { background: #333; color: #eee; }
            .stButton>button { background-color: #4CAF50; color: white; }
            </style>
        """, unsafe_allow_html=True)

# Main app UI
def main():
    st.set_page_config(page_title="🗣️ Edge TTS App", page_icon="🗣️", layout="centered")
    theme_toggle = st.toggle("🌙 Dark Mode", value=st.session_state.theme == "dark")
    st.session_state.theme = "dark" if theme_toggle else "light"
    set_theme()

    st.markdown("""
        <h1 style='text-align: center;'>🦜 Text to Speech App</h1>
        <div style='text-align: center; font-size: 2em;'>
        Let your words come alive! 🎶
        </div>
    """, unsafe_allow_html=True)

    # Language and Voice Selection
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("🌐 Choose Language", list(LANGUAGES.keys()), key="language")
    with col2:
        voice = st.selectbox("🗣️ Choose Voice", LANGUAGES[language]["voices"], key="voice")

    # PDF Upload and Text Input
    st.markdown("---")
    st.markdown("#### 📄 Upload a PDF file to extract text")
    pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    pdf_text = ""
    pdf_error = None

    if pdf_file:
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            if len(reader.pages) == 0:
                pdf_error = "The PDF file has no pages."
            else:
                extracted = []
                for page in reader.pages:
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            extracted.append(page_text)
                    except Exception as e:
                        extracted.append(f"[Error reading page: {e}]")
                pdf_text = "\n".join(extracted).strip()
                if not pdf_text:
                    pdf_error = "No extractable text found in the PDF."
                else:
                    st.success("PDF text extracted! You can edit it below.")
                    st.session_state.text = pdf_text
        except Exception as e:
            pdf_error = f"Failed to read PDF: {e}"

    if pdf_error:
        st.error(pdf_error)

    text = st.text_area("Enter text to speak (or upload a PDF):", value=st.session_state.text, height=150)

    # TTS Functions
    async def tts_to_file(text, voice):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(tmpfile.name)
            return tmpfile.name

    # Voice Preview
    with st.expander("🔊 Preview Selected Voice"):
        sample_text = LANGUAGES[language]["sample"]
        if st.button("Play Voice Preview"):
            with st.spinner("Generating preview..."):
                try:
                    audio_file = asyncio.run(tts_to_file(sample_text, voice))
                    audio_bytes = Path(audio_file).read_bytes()
                    st.audio(audio_bytes, format="audio/mp3")
                finally:
                    if audio_file and os.path.exists(audio_file):
                        os.unlink(audio_file)

    # Speak and Download
    col6, col7 = st.columns([2, 1])
    with col6:
        speak_clicked = st.button("🎤 Speak")
    with col7:
        download_clicked = st.button("⬇️ Download MP3")

    if speak_clicked or download_clicked:
        if text.strip():
            with st.spinner("Generating speech..."):
                try:
                    audio_file = asyncio.run(tts_to_file(text, voice))
                    audio_bytes = Path(audio_file).read_bytes()
                    
                    if speak_clicked:
                        st.audio(audio_bytes, format="audio/mp3")
                        st.session_state.history.insert(0, {
                            "text": text,
                            "voice": voice,
                            "audio": audio_bytes
                        })
                    
                    if download_clicked:
                        st.download_button(
                            label="Download MP3",
                            data=audio_bytes,
                            file_name="tts_output.mp3",
                            mime="audio/mp3"
                        )
                finally:
                    if audio_file and os.path.exists(audio_file):
                        os.unlink(audio_file)
        else:
            st.warning("Please enter some text.")

    # History Display
    st.markdown("---")
    with st.expander("📜 History"):
        for item in st.session_state.history:
            with st.container():
                st.write(f"Text: {item['text']}")
                st.write(f"Voice: {item['voice']}")
                st.audio(item['audio'], format="audio/mp3")

    # Footer
    st.markdown("---")
    st.caption("🦜 Powered by Edge TTS and Streamlit. | Made with ❤️")

if __name__ == "__main__":
    main()