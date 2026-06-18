import math

class Calculator:

    @staticmethod
    def square(a):
        return a * a
    
    @staticmethod
    def cube(a):
        return a * a * a
    
    @staticmethod
    def squareRoot(a):
        return math.sqrt(a)
    
resultSquare = Calculator().square(15)
print(resultSquare)

resultCube = Calculator().cube(5)
print(resultCube)

resultsquareRoot = Calculator().squareRoot(25)
print(resultsquareRoot)