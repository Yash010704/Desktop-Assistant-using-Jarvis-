import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    
    elif hour>=12 and hour<18:
        speak("goood afternooon")

    else:
        speak("good evening")

    speak("I am jarvis how may i help you")

def takecomand(): # it take microphone input from the userr and return string output
        r=sr.Recognizer()
        with sr.Microphone() as source:
             print("Listeniing...")
             r.pause_threshold=1
             audio=r.listen(source)
            
        try:
             print("Recognixing..")
             query=r.recognize_google(audio,language="en-in")
             print(f"user said:{query}\n")
        except Exception as e:
                print("Say that again please")
                return "None"
        return query

if __name__=="__main__":
    wishme()
    while   True:
        query=takecomand().lower()

        #logic to get acces 
        if "wikipedia " in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentence=2)
            speak("Acoording to wikipedia")
            speak(result)
        elif "open youtube" in query:
             webbrowser.open("youtube.com")
        
        elif "open google" in query:
             webbrowser.open("google.com")
        elif "quit" in query:
                break
