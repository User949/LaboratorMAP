from tkinter import *
from tkinter import messagebox

afisaj = Tk()
#afisaj.geometry("350x350")
afisaj.title("Salut")
Label(afisaj, text="Nume").grid(row=0) #.pack(padx=5,pady=10)
Label(afisaj, text="Prenume").grid(row=1)
nume = Entry(afisaj)
prenume = Entry(afisaj)
nume.grid(row=0, column=1)
prenume.grid(row=1, column=1)

def afiseaza_numele():
    nume_afisat = nume.get()
    prenume_afisat = prenume.get()
    messagebox.showinfo("Numele", f"Salut, {nume_afisat} {prenume_afisat}")

Button(afisaj, text="Salut", command=afiseaza_numele).grid(row=2)
mainloop()