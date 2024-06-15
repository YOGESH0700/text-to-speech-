import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as speech


text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def wishes():
    hour = datetime.datetime.now().hour
    if hour>0 and hour < 12:
        speak("Good Morning Dude!!")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon Dude!!")
    else:
        speak("Good Evening Dude!1")

    speak("Hey iam Siri, Please Tell Me How Can I Help You")



def command():
    spe = speech.Recognizer()
    with speech.Microphone() as source:
        print("Wait a Moment Listening...")
        spe.pause_threshold = 1
        main_source = spe.listen(source)

    try:
        print("Reganizing Your Voice")
        data = spe.recognize_bing(main_source,language="en-in")
        print(f"You Said: {data}\n")

    except Exception as a:
        print("Can You Say again Please")
        return None
    return data

print(command())
if __name__ == "__main__":
    wishes()
    final = command().lower()
    if "wikipedia" in final:
        speak("Please wait a moment")
        final = final.replace("wikipedia","")
        output = wikipedia.summary(final,sentence = 2)
        print(output)
        speak(output)
    elif "youtube" in final:
        webbrowser.open("www.youtube.com")
    elif "google" in final:
        webbrowser.open("www.google.com")
    elif "instagram" in final:
        webbrowser.open("www.instagram.com")
    elif "facebook" in final:
        webbrowser.open("www.facebook.com")
    elif "github" in final:
        webbrowser.open("www.github.com")
    elif "play Music" in final:
        webbrowser.open("www.open.spotify.com")
    elif "open spotify" in final:
        webbrowser.open("www.open.spotify.com")
    elif "current time" in final:
        time = datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"Sir the is {time}")







