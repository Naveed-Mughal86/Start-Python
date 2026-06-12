def greatestNum():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    # return max(a, b, c)

    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > b and c > a):
        return c



greater = greatestNum()
print(greater)