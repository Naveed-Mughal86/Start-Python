def table(num, i = 1):
    
    if(i > 10):
        return
    print(f"{num} * {i} = {num *  i}")
    table(num, i + 1)

num = int(input("Enter a number to print Table: "))
table(num)
