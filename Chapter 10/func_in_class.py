class details():
    language = "python"
    salary = "200LPA"

    def __init__(self):   # dunder method which is automatically called and starts with double underScore
        print("Hey i am learning python")

    def employeeDetail(self):       # Self is a argument here
        print(f"The language is of employee is {self.language} and salary is {self.salary}")

    @staticmethod      # used when we don't pass any argument
    def greet():
        print("Good Morning")

employee = details()
employee.greet()
employee.employeeDetail()
