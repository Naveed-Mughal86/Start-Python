num = int(input("Enter number: "))


# for i in range(1, num + 1):
#     print(" " * (num - i), end="")
#     print("*" * (2 * i - 1), end="")
#     print("")

                                    # odd star pattern using while loop 
# i = 1
# while(i <= num):
#     print(" " * (num - i), end="")
#     print("*" * (2 * i - 1), end="")
#     print("")
#     i += 1


                                        # Reverse star pattern 
for i in range(1, num + 1):
    print(" " * (i - 1), end="")
    print("*" * (num - i + 1), end="")
    print("")