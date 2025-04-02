import streamlit as st
import speech_recognition as sr
import nltk
import string

# Ensure necessary nltk data is available
nltk.download('punkt')
nltk.download('wordnet')

# Load and preprocess chatbot data
def load_data(filename):
    """Load and return the chatbot data from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().lower()
    return data

def preprocess_data(text):
    """Preprocess text by tokenizing and lemmatizing."""
    tokenizer = nltk.word_tokenize
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = tokenizer(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Sample chatbot responses
def chatbot_response(user_input):
    """Generate a response for the chatbot based on user input."""
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing fine! How about you?",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure I understand. Can you rephrase that?"
    }
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Function to transcribe speech to text
def recognize_speech():
    """Transcribe speech from microphone input to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            text = r.recognize_google(audio_text)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not get that."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

# Streamlit app
st.title("Speech-Enabled Chatbot App")

# User input method selection
input_method = st.radio("Choose input method:", ("Text", "Speech"))

if input_method == "Text":
    user_input = st.text_input("Type your message:")
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Bot: {response}")

elif input_method == "Speech":
    if st.button("Start Recording"):
        # Transcribe speech and show the response
        speech_text = recognize_speech()
        st.write("You said:", speech_text)
        
        # Get chatbot's response based on the transcribed speech
        response = chatbot_response(speech_text)
        st.write(f"Bot: {response}")

