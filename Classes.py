import tkinter as tk
import csv

window = tk.Tk()
window.title('Fi.Py')



class windowtablet():
    def __init__(self, frame, space1, space2, fipy):
        self.frame = frame
        self.space1 =space1
        self.space2 =space2
        self.fipy = fipy

    def showpage(self):
        tk.Label(master=self, text=' ', bg='White', width=20, height=3)

        tk.Label(master=self, text=' ', bg='White', width=20, height=3)

        tk.Label(master=self, text='FI.Py', bg='Orange', width=50, height=3)




window.mainloop()