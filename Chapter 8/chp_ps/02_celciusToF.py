def C_To_F():
    celcius = int(input("Enter degree Celcius: "))
    farenheit = (celcius * (9 / 5)) + 32
    return farenheit

result = C_To_F()
print(result)