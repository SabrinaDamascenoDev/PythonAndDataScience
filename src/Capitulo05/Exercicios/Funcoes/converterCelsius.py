
def converterCelsius(celsius):
    farenheit = lambda a: 9 * a / 5 + 32
    Farenheit1 = []
    for i in celsius:
        Farenheit1.append(round(farenheit(i), 2))
    return Farenheit1

Celsius = [39.2, 36.5, 37.3, 37.8]

print(converterCelsius(Celsius))
