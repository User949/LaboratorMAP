# Sa se sorteze folosing metoda bulelor

def bubbleSort(listaNumere):
    n = len(listaNumere)
    m = n
    while True:
        sortat = True
        p = m
        for i in range(p - 1):
            if listaNumere[i] > listaNumere[i + 1]:
                aux = listaNumere[i]
                listaNumere[i] = listaNumere[i + 1]
                listaNumere[i + 1] = aux
                sortat = False
                m = i + 1
        if sortat:
            break

input_x = input("Introduceti numerele: ")
x = input_x.split()
listaNumere = []
for numar in x:
    listaNumere.append(int(numar))

print(f"Lista inainte de sortare: {listaNumere}")

bubbleSort(listaNumere)

print(f"Lista sortata este: {listaNumere}")