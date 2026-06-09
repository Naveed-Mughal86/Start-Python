sub1 = int(input("Enter marks of subject 1 : "))
sub2 = int(input("Enter marks of subject 2 : "))
sub3 = int(input("Enter marks of subject 3 : "))

total_percentage = ((sub1 + sub2 + sub3) / 300) * 100
print(total_percentage)
if(total_percentage >= 40 & sub1 >= 33 & sub2 >= 33 and sub3 >= 33):
    print("You are pass")
else:
    print("Better luck next time")
