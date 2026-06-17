f = open("poem.txt")
data = f.read()
print(data)

if("twinkle" in data):
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()