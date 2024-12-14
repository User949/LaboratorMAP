# 3 nr de la tastatura. Sa se afiseze un mesaj daca acestea pot reprezenta unghiurile unui triunghi

unghi1 = float(input("Introduceti primul unghi: "))
unghi2 = float(input("Introduceti al doilea unghi: "))
unghi3 = float(input("Introduceti al treilea unghi: "))

if unghi1 > 0 and unghi2 > 0 and unghi3 > 0 and (unghi1 + unghi2 + unghi3 == 180):
    print("Aceste unghiuri pot reprezenta un triunghi.")
else:
    print("Aceste unghiuri NU pot reprezenta un triunghi.")