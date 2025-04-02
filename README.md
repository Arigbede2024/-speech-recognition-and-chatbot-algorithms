# Speech-Enabled Chatbot
This is the streamlit link [speech-recognition-and-chatbot-algorithms](https://arigbede2024--speech-recognition-and-chatbot-algor-model-7nnbiq.streamlit.app/)

A simple yet interactive chatbot powered by speech recognition and text processing using Streamlit and NLTK. This project allows users to interact with the chatbot via text input or voice commands, leveraging Google's Speech Recognition API for speech-to-text conversion.



## 🚀 Features

- 🗣 **Speech-to-Text**: Uses `speech_recognition` to convert spoken words into text.
- 💬 **Conversational AI**: Provides predefined chatbot responses.
- 🎨 **User-Friendly Interface**: Built with Streamlit for an interactive and simple UI.
- 🔍 **Natural Language Processing**: Uses `NLTK` for text preprocessing and tokenization.
- 📢 **Real-time Transcription**: Captures and transcribes voice input seamlessly.

---

## 🛠 Tech Stack

- **Python** (Primary Language)
- **Streamlit** (For Web UI)
- **SpeechRecognition** (For Speech-to-Text)
- **NLTK** (For Text Processing)
- **PyAudio** (For Microphone Access)

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
 git clone https://github.com/your-username/speech-enabled-chatbot.git
 cd speech-enabled-chatbot
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If you encounter a `PyAudio` error, install it manually:
```bash
pip install pyaudio
```
For Linux/macOS:
```bash
sudo apt-get install portaudio19-dev && pip install pyaudio
```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

This will open the chatbot interface in your browser.

---

## 🖥️ Usage

1. Select an input method (Text or Speech).
2. If using text input, type a message and receive a chatbot response.
3. If using speech, click **"Start Recording"**, speak into your microphone, and let the bot process your input.
4. The chatbot responds accordingly.

---

## 📝 Example Interactions

```
User: Hello
Bot: Hi there! How can I help you?
```

```
User: How are you?
Bot: I'm just a bot, but I'm doing fine! How about you?
```

```
User: Bye
Bot: Goodbye! Have a great day!
```

---

## 🚀 Future Enhancements

- 🤖 **Machine Learning Integration** for smarter responses.
- 🌍 **Multi-language Support** for diverse interactions.
- 🔉 **Voice Output** for a complete conversational experience.
- 📚 **Customizable Responses** to improve engagement.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any inquiries or suggestions, feel free to reach out via:


---

⭐ **If you found this project useful, please give it a star!** ⭐

