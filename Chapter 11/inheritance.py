class Employee:
    def details(self):
        print("Hey my name is PZ Mir")

class Programmer(Employee):
    print("I am inherited")

a = Programmer()
a.details()