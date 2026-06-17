# with statement automatically closes the file. You don't have to close it explicitily

with open("file.txt") as f:
    print(f.read())