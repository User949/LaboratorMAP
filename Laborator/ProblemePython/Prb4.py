# Cmmdc pentru 2 numere citite de la tastatura
x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))

def cmmdc(a, b):
    while b != 0:
        aux = a % b
        a = b
        b = aux
    return a

print(f"CMMDC dintre {x} si {y} este {cmmdc(x, y)}")