# To read any file's content
import pyttsx3

engine = pyttsx3.init()

f = open("file.txt", "rt")
data = f.read()

engine.say(data)
engine.runAndWait()

print(data)
f.close()