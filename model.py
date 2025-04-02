import streamlit as st
import speech_recognition as sr
import nltk
import random
import time
import string

# Ensure necessary nltk data is available
nltk.download('punkt')
nltk.download('wordnet')

# Load and preprocess chatbot data
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().lower()
    return data

def preprocess_data(text):
    tokenizer = nltk.word_tokenize
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = tokenizer(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens



# Sample chatbot responses
def chatbot_response(user_input):
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
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."
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
    if st.button("Speak Now"):
        user_input = recognize_speech()
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"Bot: {response}")


