with open("replaceDonkey.txt", "r") as f:
    content = f.read()

updated_file = content.replace("donkey", "####")

with open("replaceDonkey.txt", "w") as file:
    file.write(updated_file)