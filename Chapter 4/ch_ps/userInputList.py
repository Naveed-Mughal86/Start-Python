# take input of 7 fruits from user and print it 
fruits = [
    input("Enter fruit name : "),
    input("Enter fruit name : "),
    input("Enter fruit name : "),
    input("Enter fruit name : "),
    input("Enter fruit name : "),
    input("Enter fruit name : "),
    input("Enter fruit name : ")
]
print(fruits)

# 2nd way is to take input and append it in fruits
# 3rd way is to use loop

fruits = []
for i in range(7):
    fruit = input(f"Enter fruit name {i + 1} : ")
    fruits.append(fruit)
print(fruits)