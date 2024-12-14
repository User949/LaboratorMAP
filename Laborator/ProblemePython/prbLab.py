# Se citesc 5 nr de la tastatura. Sa se afiseze cel mai mare nr citit
numere = []
for i in range(5):
    numar = int(input(f"Introduceti numarul {i+1}: "))
    numere.append(numar)
print(max(numere))