import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
audio = engine.getProperty("voices")
# print(audio)
engine.setProperty("voice", audio[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Babulal. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please say again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            webbrowser.open("https://www.google.com/")

        elif "corona cases" in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/")

        elif "corona india" in query:
            webbrowser.open("https://www.covid19india.org/")


        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com") #give url for your gmail inbox

        elif "play songs" in query: # I have given a playlist link of youtube
            webbrowser.open("https://www.youtube.com/watch?v=-oTq-FfOsBk&list=RD-oTq-FfOsBk&start_radio=1")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")

        elif "open code" in query:
            path = (r"C:\Users\vibhu\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            os.startfile(path)

        elif "open download" in query:
            dwnPath = (r"C:\Users\vibhu\Downloads")
            os.startfile(dwnPath)

        elif 'play music' in query:
            music_dir = 'D:\songs' #Music directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Vaibhav. I am not able to send this email")


        elif "thank you" in query:
            exit()