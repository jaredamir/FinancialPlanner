import tkinter as tk
import csv

ExpenseList = []

window = tk.Tk()


global  Chart_frame
Chart_frame = tk.Frame()
Chart_frame.grid(row=0, column=0)


with open('Expenses.csv', 'r') as file:
    Expenses = csv.reader(file)

    for row in Expenses:
        ExpenseList.append(row)

Fi_py = tk.Label(master=Chart_frame, text='FI.Py', bg='Orange', width=50, height=3)
Fi_py.grid(row=0, column=1)
space = tk.Label(master=Chart_frame, text=' ', bg='White', width=20, height=3)
space.grid(row=0, column=0)
space_2 = tk.Label(master=Chart_frame, text=' ', bg='White', width=20, height=3)
space_2.grid(row=0, column=2)

for i in range(len(ExpenseList)):
    expense_name = ExpenseList[i][0]
    expense_name =tk.Label(master=Chart_frame, text=str(expense_name))
    expense_name.grid(row=i+1, column=0)

    price = ExpenseList[i][1]
    price = tk.Label(master=Chart_frame, text=str(price))
    price.grid(row=i+1, column=1)

    w_m = ExpenseList[i][2]
    w_m = tk.Label(master=Chart_frame, text=str(w_m))
    w_m.grid(row=i+1, column=2)


list_len = len(ExpenseList)

button = tk.Button(master=Chart_frame, text="Add Expense")
button.grid(row=(list_len + 2), column=1)

button_2 = tk.Button(master=Chart_frame, text="Edit Expense")
button_2.grid(row=(list_len + 3), column=1)

button_3 = tk.Button(master=Chart_frame, text="Back")
button_3.grid(row=(list_len + 4), column=1)

window.mainloop()

#read csv, append into organized list, row by row take name(add widget) then price(add widget) then weekly(add widget),  repeat down the list


"""
window = tk.Tk()
window.title('tester')

window.rowconfigure(0, min=50, weight=2)
window.columnconfigure(0, min=50, weight=2)

Test_frame = tk.Frame()
Test_frame.grid(row=0, column=0)

class Expense_name:
    def __init__(self):
        Enum = tk.Label(master=Test_frame, text=(self))

        def egrid():
            Enum.grid(column=0, row=[i])

class Price:
    def __init__(self):
        Prc = tk.Label(master=Test_frame, text=(self))

        def egrid():
            Prc.grid(column=2, row=[i])

class w_or_m:
    def __init__(self):
        WM = 
        WM = tk.Label(master=Test_frame, text=(self))

        def egrid():
            WM.grid(column=2, row=[i])
"""







#window.mainloop()
