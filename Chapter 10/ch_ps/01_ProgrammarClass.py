# class Programmar:
#     language = "py"
#     salary = "120LPA"
#     company = "Microsoft"

# employeeData = Programmar()
# employeeData.name = "Naveed"
# print(employeeData.name, employeeData.language, employeeData.salary, employeeData.company)

class Programmar:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
employeeData = Programmar("Naveed", 1200000, 23415)
print(employeeData.name, employeeData.salary, employeeData.pin, employeeData.company)