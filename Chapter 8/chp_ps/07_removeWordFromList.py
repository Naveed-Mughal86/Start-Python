def removeWordFromList(myList, word):
    n = []
    for item in myList:
        if(not(item == word)):
            n.append(item.strip(word))
        return n
myList = ["Hassan", "Haseeb", "Naveed"]

print(removeWordFromList(myList, "an"))