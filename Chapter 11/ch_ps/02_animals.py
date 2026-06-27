class Animals:
    print("We love animals")

class Pets(Animals):
    print("We have pets here")

class Dog(Pets):
    def bark(self):
        print("The dog is barking in the mid night")

a = Dog()
a.bark()