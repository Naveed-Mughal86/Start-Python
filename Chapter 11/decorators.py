# in which we want to show the class attribute and not the onject attribute
# so in this case we use class method
class Employee:
    a = 1
    # def show(self):
    #     print(f"The value of class attribute is {self.a}")

    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

result = Employee()
result.a = 45
result.show()