from tkinter import *
from tkinter import messagebox
from math import sqrt

afisaj = Tk()
afisaj.title("Calculator")
Label(afisaj, text="Numar 1:").grid(row=0)
Label(afisaj, text="Numar 2:").grid(row=1)
numar1 = Entry(afisaj)
numar2 = Entry(afisaj)

label_rezultat = Label(afisaj, text="Rezultat:")
label_rezultat.grid(row=2)

numar1.grid(row=0, column=1)
numar2.grid(row=1, column=1)

def inmultire():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = numarul1 * numarul2
    label_rezultat.config(text=f"Rezultat: {rez}")

def impartire():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = numarul1 / numarul2
    label_rezultat.config(text=f"Rezultat: {rez}")

def adunare():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = numarul1 + numarul2
    label_rezultat.config(text=f"Rezultat: {rez}")

def scadere():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = numarul1 - numarul2
    label_rezultat.config(text=f"Rezultat: {rez}")

def radical():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = sqrt(numarul1)
    rez2 = sqrt(numarul2)
    label_rezultat.config(text=f"Rezultat: {rez}, {rez2}")

def ridicareaLaPutere():
    global label_rezultat
    numarul1 = int(numar1.get())
    numarul2 = int(numar2.get())
    rez = pow(numarul1, numarul2)
    label_rezultat.config(text=f"Rezultat: {rez}")

def stergere():
    global label_rezultat
    label_rezultat.config(text="Rezultat: ")

Button(afisaj, text="*", command=inmultire).grid(row=3)
Button(afisaj, text="/", command=impartire).grid(row=3, column=1)
Button(afisaj, text="+", command=adunare).grid(row=4)
Button(afisaj, text="-", command=scadere).grid(row=4, column=1)
Button(afisaj, text="√", command=radical).grid(row=5)
Button(afisaj, text="^", command=ridicareaLaPutere).grid(row=5, column=1)
Button(afisaj, text="CLEAR", command=stergere).grid(row=6)
mainloop()