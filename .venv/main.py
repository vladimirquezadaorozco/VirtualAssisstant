import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_Command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')

            else:
                print('Jarvis not in commmand')
    except:
        pass

    return command

def runJarvis():
    command = take_Command()
    print(command)
    if 'play' in command:
        talk('playing')
        print('playing')

runJarvis()