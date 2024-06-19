import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyaudio
import wave
import ecapture as ec

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
audio = pyaudio.PyAudio()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def run_alexa():
    command = take_command()
    print(command)
    if 'play on youtube' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search on wikipedia' in command:
        talk('Please type to search')
        In = input("Search Wikipedia/Google: ")
        result = wikipedia.summary(In, sentences = 2)
        print(result)
        talk(result)
        
    elif 'stop' in command:
        exit()
    
    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "Alexa Camera ", "img.jpg")
        
    elif 'time' in command:
        strTime = datetime.datetime.now()
        curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
        talk(f" the time is {curTime}")
        print(curTime)
        
    elif 'search on google' in command:
        import wikipedia as googleScrap
        command = command.replace("alexa","")
        command = command.replace("google search","")
        command = command.replace("google","")
        speak("This is what I found on google")
        
        try:
            pywhatkit.search(command)
            result = googleScrap.summary(command,1)
            speak(result)

        except:
            speak("No speakable output available")

    else:
        talk('Please say the command again.')

while True:
    run_alexa()