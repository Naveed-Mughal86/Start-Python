class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# myCar = Car("Toyota", "Corolla")
# print(myCar.brand, myCar.model)

ev = Electric_Car("Toyota", "Corolla", "220kv")
print(ev.brand, ev.model, ev.battery_size)
 