import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

 

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greet():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Hasan!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Night") 
    speak("I'm omega " )
    speak("please tell me how may I help you") 


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query    






if __name__=="__main__":
    Greet()
    while True:
        query=takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query= query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open('Google.com')

        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open('facebook.com') 

        elif 'open github' in query:
            speak("Opening github")
            webbrowser.open('github.com')  

        elif 'Your name' in query:
            speak("My name is Omega.")

        elif 'Are you single' in query:
            speak("Its complicated !")     
             




        elif 'play music' in query:
            music_dir = 'C:\\Users\\NAJMUL\\Music\\arijit singh' 
            song = os.listdir(music_dir) 
            print("Enjoy the song...")
            os.startfile(os.path.join(music_dir, song[9]))

        elif 'the time' in query:
            NowTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {NowTime}')

        elif 'quit' in query:
            speak("Okay sir.")
            exit()   
