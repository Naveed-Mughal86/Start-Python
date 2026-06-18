class Employee:
    def __init__(self):
        print("Hey my name is Employee")
    
class Programmer(Employee):
    def __init__(self):
        super().__init__()

a = Programmer()
