# Factorialul unui nr citit de la tastatura

def factorial(n):
    rez = 1
    for i in range(1, n + 1):
        rez *= i
    return rez

x = int(input("Introduceti un numar: "))
print(f"Factorialul lui {x} este {factorial(x)}")