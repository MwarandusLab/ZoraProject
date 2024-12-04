import speech_recognition as sr

# Initialize recognizer class
recognizer = sr.Recognizer()

# Function to capture audio and convert it to text
def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing...")

    try:
        # Convert audio to text using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Main loop
if __name__ == "__main__":
    while True:
        recognize_speech_from_mic()
