import pyttsx3  # Text-to-speech engine
import speech_recognition as sr  # For speech recognition
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Store user details for interaction
user_details = {
    "name": "Brian",
    "location": "Nairobi",
    "age": "19",
    "hobby": "creating smart devices",
    "favorite_color": "blue",
}

# Function to set a female voice
def set_female_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower():  # Search for a female voice
            engine.setProperty('voice', voice.id)
            break
    else:
        engine.setProperty('voice', voices[1].id)  # Use the second voice as fallback
    engine.setProperty('rate', 150)  # Adjust speed
    engine.setProperty('volume', 0.9)  # Adjust volume

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands in continuous conversation mode
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")
                respond_to_command(command)
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Can you repeat?")
            except sr.RequestError:
                speak("Could not request results. Please check your internet connection.")
            except sr.WaitTimeoutError:
                speak("I didn't hear anything. I'm still here, waiting for your command.")

# Function to respond to user commands
def respond_to_command(command):
    if "time" in command:
        current_time = time.strftime("%I:%M %p")  # 12-hour format with AM/PM
        speak(f"The current time is {current_time}.")
    
    elif "your name" in command or "who are you" in command:
        speak("I am Zoro, your virtual assistant.")
    
    elif "my name" in command:
        speak(f"Your name is {user_details['name']}.")
    
    elif "where do i live" in command:
        speak(f"You live in {user_details['location']}.")
    
    elif "how old am i" in command:
        speak(f"You are {user_details['age']} years old.")
    
    elif "what is my hobby" in command:
        speak(f"Your hobby is {user_details['hobby']}.")
    
    elif "favorite color" in command:
        speak(f"Your favorite color is {user_details['favorite_color']}.")
    
    elif "how are you" in command:
        speak("I am doing well, thank you! How about you?")
    
    elif "what is your favorite color" in command:
        speak("I like all colors, but I find blue to be very calming.")

    elif "ask me something" in command:
        speak("Okay! What is your favorite movie?")

    elif "what's the weather" in command:
        speak("I currently don't have access to the internet for weather updates.")

    elif "tell me a joke" in command:
        speak("Why don’t skeletons fight each other? Because they don’t have the guts!")

    elif "goodbye" in command or "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    
    else:
        speak("I am not sure how to respond to that. But I'm here to learn!")

# Main function to start listening
if __name__ == "__main__":
    set_female_voice()  # Set a female voice when starting
    speak("Voice Assistant Zoro is running... I am ready for our conversation.")
    listen_for_command()
