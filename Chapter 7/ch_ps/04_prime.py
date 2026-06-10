num = int(input("Enter a number to check if its prime or not : "))
for i in range(2, num):
    if(num % i == 0):
        print("It's not a prime number ❌")
        break
else:
        print("It's a prime number ✅")
    