# pip install pyttsx3
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    rate= engine.getProperty('rate')
    engine.setProperty('rate',rate - 50)
    engine.say(text)
    engine.runAndWait()

if __name__=='__main__':
    print("Welcome to roboSpeaker 1.1 Created by Trez")
    while True:
        x = input("Enter Whatever you want me to speak: ")
        if x.lower()=="q":
            break
        speak(x)


