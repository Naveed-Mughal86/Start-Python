import pyttsx3
letter = '''Dear <|Name|>,
You are selected
<|Date|>'''

# print(letter)
name = input("Enter Name ")
date = input("Enter Date ")

engine = pyttsx3.init()
engine.say(name, date)
engine.runAndWait()

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))