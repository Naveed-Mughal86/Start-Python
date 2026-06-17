words = ["donkey", "fool", "people"]

with open("replaceDonkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("replaceDonkey.txt", "w") as file:
          file.write(content)