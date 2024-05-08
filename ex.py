import tkinter as tk

def Bonjour(a):
    message.config(text="Bonjour "+ texte.get()+" !!" if texte.get() else "Bonjour Tout le monde!!")

window = tk.Tk()
window.title("Mon premier interface Tkinter")
window.geometry("500x500")

container = tk.Frame(window, width=400, height=300)
container.place(x=25, y=100)

label = tk.Label(container, text='Entrer votre nom: ')
label.grid(row=0,column=0)

texte = tk.Entry(container, width=20)
texte.grid(row=0,column=1, padx=50)


bouton = tk.Button(container, text="Cliquez!!!", command=Bonjour)
bouton.grid(row=1, pady=10)
texte.bind('<Return>', (lambda e: Bonjour(e)))


message = tk.Label(container, text="Bonjour Tout le monde!!", fg="black")
message.grid(row=1, column=1)



window.mainloop()



    # dec = dectobin(bin)
    
    # return (bin,dec)

# def message(window,res):
#     imprim = tk.Frame(window)
#     imprim.grid(row=3,column=1)

#     imprim1 = tk.Label(imprim)
#     imprim1.config(text="Valeur numérique :"+ res[0] )

#     imprim2 = tk.Label(imprim)
#     imprim2.config(text="Valeur décimale :"+ res[1] )