# Det suma si media aritmetica a unei liste citite
input_x = input("Introduceti numerele: ")

x = input_x.split()

listaNumere = []

for numar in x:
    listaNumere.append(float(numar))

s = 0
for i in listaNumere:
    s += i
if len(listaNumere) > 0:
    media = s / len(listaNumere)
else:
    media = 0
print(f"Suma numerelor este: {s}")
print(f"Media aritmetica este: {media}")