
# Python Voice Assistant

A modular and voice-driven assistant built with Python, this project integrates speech recognition, real-time APIs, email automation, natural language processing, and scheduling. It emphasizes voice-based interactivity, secure data handling, and extensible design suitable for future enhancements.

## Theoretical Background
This project integrates multiple core disciplines in computer science:

- **Speech Recognition**: Utilizes Google’s Speech Recognition API to transcribe user voice commands into text.
- **Text-to-Speech (TTS)**: Uses `pyttsx3` for converting text responses into speech output through system voices.
- **Natural Language Processing (NLP)**: Employs `spaCy` to process and interpret voice commands using syntactic analysis and token parsing.
- **API Integration**: Retrieves real-time weather data via Tomorrow.io's API, demonstrating client-server communication and data handling.
- **Web Automation**: Opens relevant websites using the built-in `webbrowser` module based on recognized voice commands.
- **Email Automation**: Sends emails using Gmail’s SMTP services via Python’s `smtplib` and `email.message`.
- **Task Scheduling**: Integrates `schedule` to trigger reminders after user-defined intervals, enabling time-bound voice tasks.

## Features

- Voice recognition (SpeechRecognition + Google Speech API)
- Text-to-speech interaction (pyttsx3)
- Real-time weather updates via Tomorrow.io
- Wikipedia-powered question answering
- Web search and site launching (Google, YouTube, Wikipedia, News)
- Email composition and delivery through Gmail
- Reminder scheduling via voice
- Command parsing using `spaCy` NLP

## System Requirements

- Python 3.9 or higher recommended
- OS: Windows 10/11, Ubuntu Linux 20.04+, macOS (limited support for TTS engines)
- Microphone enabled for voice input
- Internet access required for API and Wikipedia functionality

## Installation

Install the required libraries using:

```bash
pip install python-dotenv requests pyttsx3 SpeechRecognition pyaudio wikipedia spacy schedule
python -m spacy download en_core_web_sm
```

## Configuration

Create an `id.env` file in your project directory to store your API and email credentials securely:

```env
TOMORROW_API_KEY=your_tomorrow_io_api_key
EMAIL_ADDRESS=your_gmail_address
EMAIL_PASSWORD=your_gmail_app_password
```

> Important: If Gmail has 2FA enabled, generate an App Password and use that instead of your main email password.

## Usage

To run the voice assistant:

```bash
python code.py
```

### Supported Commands

- Ask about current date and time
- Get weather updates by city
- Search queries on Google
- Open websites: YouTube, Google, Wikipedia, News
- Send emails via Gmail through voice input
- Set reminders with spoken intervals
- Ask factual questions
- Hear a joke

### Example Interaction

**User:** What's the weather in Delhi?  
**Assistant:** The temperature in Delhi is 35°C with Mostly Clear skies.


## Troubleshooting

**PyAudio installation fails on Windows:**

```bash
pip install pipwin
pipwin install pyaudio
```

**TTS issues on Linux:**

```bash
sudo apt-get update
sudo apt-get install espeak
```

## Future Improvements

- Add GUI interface (Tkinter or PyQt) for visual accessibility
- Integrate Google Calendar for event management
- Implement command history and feedback logging
- Add voice authentication
- Enable offline speech recognition with local models
- Expand NLP using transformer-based models (BERT, etc.)
- Multilingual support
- Dockerize for deployment across environments
