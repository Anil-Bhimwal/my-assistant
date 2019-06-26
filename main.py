import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# to change voice 0==>1
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """ Function to wish according to time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I'm your Assistant Sir, How may i help you?")


def takeCommand():
    """This function will take Command from User using microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say That Again Please....")
        return "None"
    return query


def sendEmail(id, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmailid', 'password')
    server.sendmail('recieve address', to, content)
    server.clode()


if __name__ == '__main__':
    wishMe()
    query = takeCommand().lower()

    # task 1: wikipedia

if 'wikipedia' in query:
    speak('Searching Wikipedia..')
    query = query.replace("tell me about", "")
    # return to statements
    results = wikipedia.summary(query, sentences=3)
    speak("According to wikipedia")
    print(results)
    speak(results)
elif 'open youtube' in query:
    webbrowser.open("youtube.com")
elif 'open google' in query:
    webbrowser.open("google.com")
elif 'open coding ninjas' in query:
    webbrowser.open("https://codingninjas.in/")
elif 'open leetcode' in query:
    webbrowser.open("https://leetcode.com/")
elif 'play music' in query:
    music_dir = 'F:\\musicfiles'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
elif 'time' in query:
    timenow = datetime.datetime.now().strftime("HH:MM:SS")
    speak(f"Sir, the time is {timenow}")

elif 'open code' in query:
    vscode = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(vscode)
elif 'email to anil' in query:
    try:
        speak("What should i say")
        content = takeCommand()
        to = "8175@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry I can't do")