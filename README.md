# Text to Speech Application

A Streamlit-based Text-to-Speech application that converts text and PDF content into speech using Microsoft's Edge TTS service. This application provides a user-friendly interface for converting text and documents into natural-sounding speech.

## Features

- 📝 Text-to-Speech Conversion:
  - Support for multiple languages
  - Multiple voice options per language
  - Adjustable speech rate and volume
- 📄 PDF Document Support:
  - Convert entire PDF documents to speech
  - Extract text from PDFs automatically
  - Support for multiple pages
- 🎛️ User Interface:
  - Clean and intuitive Streamlit interface
  - Real-time preview of speech
  - Download functionality for generated audio
- 🌐 Cloud Integration:
  - Uses Microsoft Edge TTS service
  - High-quality neural voices
  - Automatic language detection

## Supported Languages

- English (US)
  - Voices: Aria Neural, Guy Neural
- English (UK)
  - Voices: Libby Neural, Ryan Neural
- More languages can be added by modifying the configuration

## Prerequisites

- Python 3.8 or higher
- Streamlit (>=1.28.0)
- Edge-TTS (>=2.0.0)
- PyPDF2 (>=3.0.1)
- Requests (>=2.31.0)
- python-dotenv (>=1.0.0)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/text-to-speech-app.git
   cd text-to-speech-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Unix/macOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run streamlit_tts_app.py
   ```

2. Open your web browser and navigate to the displayed URL (usually http://localhost:8501)

3. Application Interface:
   - Select your preferred language from the dropdown
   - Choose your desired voice
   - Enter text or upload a PDF file
   - Adjust speech rate and volume
   - Click "Convert" to generate speech
   - Download the generated audio file

### Text Input
- Enter any text in the text area
- The application will automatically select the appropriate voice based on your language selection
- You can preview the speech before downloading

### PDF Upload
- Click the "Upload PDF" button
- Select your PDF file
- The application will automatically extract text and convert it to speech
- Large PDFs may take longer to process

## Environment Variables

Create a `.env` file in the project root with any required environment variables:
```
# Add any required environment variables here
```

## Troubleshooting

### Common Issues

1. **Audio Not Playing**
   - Ensure your browser's audio is not muted
   - Check if your speakers are working
   - Try refreshing the page

2. **PDF Upload Fails**
   - Ensure the PDF is not password protected
   - Try uploading a different PDF
   - Check if the PDF is corrupted

3. **Voice Not Available**
   - Ensure you have selected a valid language
   - Check if the Edge TTS service is available
   - Try selecting a different voice

### Error Messages

- `Voice not found`: The selected voice is not available for your language
- `Invalid PDF`: The uploaded file is not a valid PDF
- `Network Error`: Connection to Edge TTS service failed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Microsoft Edge TTS service for providing high-quality neural voices
- Streamlit for the excellent web framework
- PyPDF2 for PDF processing capabilities

## Contact

Project Link: [https://github.com/Yavic2024/text-to-speech-app](https://github.com/Yavic2024/text-to-speech-app)
