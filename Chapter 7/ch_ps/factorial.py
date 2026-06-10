num = int(input("Enter a number to find factorial: "))

fact = 1
for i in range(1, num + 1):
    fact = i * fact
print(fact)