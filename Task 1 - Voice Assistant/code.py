import os     # Used to work with environment variables like API keys or email credentials
import requests    # Helps fetch data from websites or APIs (e.g., weather info)
import pyttsx3     # Used for text-to-speech, so that the assistant can "talk".
import speech_recognition as sr   # Used to capture and understand voice commands.
import webbrowser  # Opens a web page in your default browser used for search.
import wikipedia   # Lets you search and get summaries from Wikipedia
import smtplib     # Sends emails through your Gmail account
import spacy       # For NLP parsing
import schedule    # For scheduling reminders
import time    # Required for schedule loop
from email.message import EmailMessage # Helps create the structure of the email (To, Subject, Body)
from datetime import datetime     # Used to get and format current time and date
from dotenv import load_dotenv    # Loads sensitive info (like API keys) from a hidden .env file

# Load spaCy's small English NLP model for understanding user input
nlp = spacy.load("en_core_web_sm")

# Loads API key and email credentials from a hidden file to keep them secure.
# Make sure to create a file named 'id.env' in the same directory with the following content:
load_dotenv("id.env")
API_KEY = os.getenv("TOMORROW_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Initialize speech engine for text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Set speaking speed  

# Speak and display reply
def speak(text):
    print(f"> {text}")   # Show assistant's reply on screen
    engine.stop()      # Stop any ongoing speech
    engine.say(text)      # Queue new text to speak
    engine.runAndWait()   # Speak the text

# Listen to user's voice and convert it to text
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  # Opens the microphone to listen
        recognizer.adjust_for_ambient_noise(source, duration=0.8)   # Reduce background noise
        speak("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)  # Listen for user's command
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()  # Convert to lowercase for easier matching
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that.")
            return ""
        except sr.WaitTimeoutError:
            speak("I didn’t hear anything.")
            return ""
        except sr.RequestError:
            speak("Voice service isn’t working right now.")
            return ""

# Get current weather of a city using Tomorrow.io API
def get_weather(city):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        values = response.json()["data"]["values"]  # Extract weather data from the response
        temp = values["temperature"]
        code = values["weatherCode"]
        # Map weather codes to human-readable conditions
        code_map = {
            1000: "Clear", 1100: "Mostly Clear", 1101: "Partly Cloudy", 1102: "Mostly Cloudy",
            1001: "Cloudy", 4000: "Drizzle", 4200: "Light Rain", 4001: "Rain",
            4201: "Heavy Rain", 5000: "Snow", 5100: "Light Snow", 5001: "Flurries",
            5101: "Heavy Snow", 8000: "Thunderstorm"
        }
        condition = code_map.get(code, "Unknown Weather")
        speak(f"The temperature in {city} is {temp}°C with {condition}.")
    except Exception:
        speak("Couldn’t fetch the weather right now.")

# Function to answer questions using Wikipedia
def answer_question(query):
    try:
        result = wikipedia.summary(query, sentences=2) # Get a brief summary of the topic
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("That topic has multiple meanings. Could you clarify?")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything relevant to that topic.")
    except Exception:
        speak("Something went wrong while searching.")

# Function to open websites based on user command
def open_website(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "chrome" in command or "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Launching Google.")
    elif "wikipedia" in command:
        webbrowser.open("https://www.wikipedia.org")
        speak("Opening Wikipedia.")
    elif "news" in command:
        webbrowser.open("https://news.google.com")
        speak("Opening news headlines.")
    # if the website is not listed, ask the user to specify
    else:
        speak("Please specify a website to open.")

# Function to send an email using Gmail
def send_email():
    speak("Who should I send the email to?")
    recipient = get_voice_input()
    speak("What's the subject?")
    subject = get_voice_input()
    speak("What should the message say?")
    message = get_voice_input()
    # Validate inputs
    if not all([recipient, subject, message]):
        speak("I couldn’t create the email. Try again.")
        return
    # Create the email message
    email = EmailMessage()
    email["From"] = EMAIL_ADDRESS
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(email)
        speak("Email sent successfully.")
    except Exception:
        speak("Something went wrong while sending the email.")

# Function to set a reminder
def set_reminder():
    speak("What should I remind you about?")
    task = get_voice_input()
    speak("In how many minutes?")
    try:
        minutes = int(get_voice_input())
        # Schedule the reminder using the schedule library
        schedule.every(minutes).minutes.do(lambda: speak(f"Reminder: {task}"))
        speak(f"Okay! I'll remind you about '{task}' in {minutes} minutes.")
    except ValueError:
        speak("That didn’t sound like a valid number.")

# Main function to run the voice assistant
def main():
    speak("Hey there! I'm your voice assistant.")
    speak("I can tell you the time and date, check the weather, look stuff up on Wikipedia, search the web, open websites like YouTube or Google, send emails, set reminders, and even crack a joke if you need a laugh.")
    speak("So... what can I do for you?")

    while True:
        command = get_voice_input()
        doc = nlp(command)  # NLP parsing

        if not command:
            continue
        elif any(exit_word in command for exit_word in ["exit", "quit", "bye"]):
            speak("See you soon!")
            break
        elif "hello" in command or "hi" in command:
            speak("Hello there! What would you like me to do?")
        elif "how are you" in command:
            speak("I'm functioning perfectly. Thanks for asking!")
        elif "who build you" in command:
            speak("I was created by Sakshi")
        elif any(token.lemma_ == "time" or token.lemma_ == "date" for token in doc): 
            now = datetime.now()
            # Get current date and time
            speak(f"It’s {now.strftime('%A, %B %d, %I:%M %p')}")
        elif any(token.lemma_ == "weather" or token.lemma_ == "temperature" for token in doc): 
            # Get the city name from the command or ask for voice input
            city = command.split("in", 1)[-1].strip() if "in" in command else get_voice_input()
            if city:
                get_weather(city)
        elif "search" in command:
            # Get the search query from the command or ask for voice input
            query = command.split("search", 1)[-1].strip() or get_voice_input()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Searching for {query}")
        elif "open" in command or "launch" in command:
            open_website(command)
        elif "email" in command or "mail" in command:
            send_email()
        elif "joke" in command:
            speak("Why don’t programmers like nature? Because it has too many bugs!...haha!")
        elif "remind" in command or "reminder" in command:
            set_reminder()  
        else:
            answer_question(command)

        # check scheduled reminders
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
