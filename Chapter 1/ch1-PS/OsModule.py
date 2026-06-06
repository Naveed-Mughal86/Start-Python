import os
import pyttsx3

engine = pyttsx3.init()
directory_path = '/'
contents = os.listdir(directory_path)

print(contents)
    
engine.say(contents)
engine.runAndWait()
