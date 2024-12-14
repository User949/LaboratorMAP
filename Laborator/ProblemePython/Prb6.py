# Det daca un nr citit de la tastatura este prim

def prim(a):
    if a < 2:
        return 0
    if a == 2:
        return 1
    if a > 2 and a % 2 == 0:
        return 0
    d = 3
    while d * d <= a:
        if a % d == 0:
            return 0
        d += 2
    return 1

x = int(input("Introduceti un numar: "))
if prim(x) == 1:
    print(f"{x} este numar prim!")
else:
    print(f"{x} nu este numar prim!")