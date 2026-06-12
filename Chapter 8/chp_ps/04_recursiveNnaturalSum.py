def sumOFNaturalNum(num):
    if(num == 1):
        return 1
    return num + sumOFNaturalNum(num - 1)

num = int(input("Enter n natural Number: "))
print(f"The sum of n natural Numbers is : {sumOFNaturalNum(num)}")