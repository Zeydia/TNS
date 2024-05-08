import tkinter as tk
from functions import *

fields = 'Scc', 'Nbits', 'Convert', 'Ve'


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Convetisseur CAN')
    window.geometry('300x250')


    ents = form(window, fields)
    window.bind('<Return>', (lambda ev , e=ents,w=window: fetch(w,e)))

    boutton(window,ents)
    message(window)



    window.mainloop()