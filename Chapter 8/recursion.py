# Factoril with For loop
# num = int(input("Enter a number : "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i
# print(fact)

# Factorial using Recursion

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)

# a = factorial(5)
# print(a)

n = int(input("Ener a number to find Fatorial : "))
print(f"Factorial of this number is : {factorial(n)}")