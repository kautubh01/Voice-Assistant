import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""

    return query.lower()

def respond_to_query(query):
    if "hello" in query:
        response = "Hello! How can I assist you today?"
    elif "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    elif "date" in query:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        response = f"Today's date is {today}."
    elif "search for" in query:
        search_term = query.split("search for")[-1].strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
        response = f"Searching for {search_term} on the web."
    else:
        response = "I am not sure how to help with that."

    return response

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        query = listen()
        if query == "":
            continue
        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break
        response = respond_to_query(query)
        speak(response)

if __name__ == "__main__":
    main()
