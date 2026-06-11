# this is the function definition where all the instructions are executed
def average():
    a = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))
    c = int(input("Enter number 3 : "))

    avg = (a + b + c) / 3
    print(avg)

# average()   # this is the function call

# write a program to greet user with "Good Day" using function

def greetUser():
    name = input("Enter your name : ")
    print(f"Have a Good Day {name}")

greetUser()