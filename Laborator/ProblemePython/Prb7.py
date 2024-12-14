# Det daca un an citit de la tastatura este an bisect
def anBisect(n):
    cnt = 0
    if n % 4 == 0:
        cnt += 1
    if n % 100 == 0:
        cnt += 1
        if n % 400 == 0:
            cnt += 1
    return cnt

x = int(input("Introduceti un an: "))
rez = anBisect(x)
if rez == 3 or rez == 1:
    print(f"{x} este un an bisect!")
else:
    print(f"{x} nu este un an bisect!")
