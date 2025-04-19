# Mini-virtual-voice-assistant


This is a basic Python voice assistant that can:
- Tell the current time 
- Open websites like Google   
- Tell you a joke 
- Open simple applications like Notepad, Calculator, and Clock 
- Respond to basic questions  

## 🔧 Features
- **Voice Output:** Uses `pyttsx3` for text-to-speech.
- **Voice Input:** Captures microphone input using `sounddevice`.
- **Speech Recognition:** Converts spoken input into text with Google's speech recognition.
- **Joke API:** Pulls a random joke using `pyjokes`.
- **Web & App Integration:** Can open Google, Clock, Calculator, Notepad, etc.

## 🛠️ Requirements

Install the required libraries using pip:

```bash
pip install sounddevice numpy speechrecognition pyttsx3 pyjokes
```

You’ll also need:
- Python 3.6 or later
- A working microphone 🎤
- Internet access (for speech recognition)

## ▶️ How to Run

1. Save the script as `assistant.py`.
2. Run the file using:
   ```bash
   python assistant.py
   ```
3. Speak into your microphone when prompted. The assistant will respond based on your input.

## 🧠 Voice Commands You Can Try

- “What’s the time?”
- “Open Google”
- “Tell me a joke”
- “Open calculator / notepad / clock”
- “What’s your name?”

## 📌 Notes

- This assistant uses the default system microphone and speaker.
- Speech recognition requires an active internet connection.
- Limited app support — more can be added in the `open_app()` function.

## 📄 License

This project is for educational purposes. Feel free to modify and expand it!

---
