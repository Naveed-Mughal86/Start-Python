class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        print(f"{self.brand} and {self.model}")

myCar = Car("Toyota", "Corolla")
print(myCar.brand, myCar.model)
myCar.full_name()