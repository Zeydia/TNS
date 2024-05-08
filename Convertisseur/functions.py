import tkinter as tk
from can import *


def fetch(window,e):

    Ve, nbreBits, Scc, convert = (e[i].get() for i in e)
    var = (Ve, nbreBits, Scc, convert)

    affiche(message(window),var)


def form(window, fields):
    form = tk.Frame(window)
    form.grid(row=0)
    entries = {}

    for field in fields:
        row = tk.Frame(form)
        row.pack(side=tk.TOP, fill='x', padx=5, pady=5)

        lab = tk.Label(row, width=10, text=field, anchor='w')
        lab.pack(side='left')

        ent = tk.Entry(row)
        ent.pack(side='right',fill='x')

        entries[field] = ent
    

    return entries
    


def boutton(window,entries):
    bouttons = tk.Frame(window)
    bouttons.grid(row=1, column=0, pady=10, padx=10)

    save = tk.Button(bouttons, text='Calculer', pady=5, padx=5, command=(lambda e=entries,w=window: fetch(w,e) ))
    save.pack(side='left')


    quitter = tk.Button(bouttons, text='Quitter', padx=5, pady=5, command=window.quit)
    quitter.pack()



def Calcul(entries):
    
    if '' not in entries: 
        Scc, nbreBits, convert, Ve = (float(entry) for entry in entries)
    else: 
        return ''

    N = convertisseur_can(Ve, nbreBits, input_voltage_range=(0,Scc),convertion=convert)
    binN = dectobin(N)

    return (N,binN)


def message(window):
    champ1 = tk.Frame(window)
    champ1.grid(row=3)

    la1 = tk.Label(champ1, text="Valeur numérique :")
    la1.pack(side=tk.LEFT, fill='x')

    champ2 = tk.Frame(window)
    champ2.grid(row=4)

    la2 = tk.Label(champ2, text="Valeur binaire :")
    la2.pack(side='left')
    
    return (champ1,champ2)

def affiche(window, e):
    imprim1 = tk.Label(window[0])
    imprim1.pack(side=tk.LEFT)

    if '' in e:
        imprim1.config(text='Donnée(s) manquante(s)')
    else:
        imprim1.config(text=Calcul(e)[0])

    imprim2 = tk.Label(window[1])
    imprim2.pack(side=tk.LEFT)

    if '' in e:
        imprim2.config(text='Donnée(s) manquante(s)')
    else:
        imprim2.config(text=Calcul(e)[1])
