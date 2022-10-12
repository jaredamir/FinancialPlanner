import tkinter as tk

#Basics
"""
window = tk.Tk() #creates the window


greeting = tk.Label( #tk.label creates text widget,
    text='python, rocks',
    foreground='purple', #forground sets text color (also can type fg)
    background='black', #background gives colored boarder behind text (also can type bg)
    width=10,
    height=10) #width and height are not measured exactly the same

greeting.pack() #.pack adds varible to window

button = tk.Button(
    text='Click Here',
    width=25,
    height=5,
    bg='white',
    fg='black')
button.pack()

entry = tk.Entry(
    fg='black',
    bg='white',
    width=50
)
entry.insert(0,'$')
entry.pack()
name = entry.get() #.get is how to  retrieve a entry, set it equal to a variable (LEARN)

frame_a = tk.Frame() #order matters with frames
frame_b = tk.Frame()
label_a = tk.Label(master=frame_a, text='frame A')
label_a.pack()
label_b = tk.Label(master=frame_b, text='frame A')
label_b.pack()

frame_a.pack()
frame_b.pack()

tk.Label(text='one time use text').pack() #you dont need to make a seperate veriable

window.mainloop() #listens for action  on window, does not execute rest of code till done
"""






#Place
"""
window = tk.Tk()
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text ="0,0", bg='white', fg='black')
label1.place(x=0, y=0) #.place is not responsive to window resizing
#.place is not the best to use
label2 = tk.Label(master=frame, text="75,75", bg='red')
label2.place(x=75, y=0)
"""




#.Grid
"""

window = tk.Tk()
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75) #configure gives parameters for resize
    window.rowconfigure(i, weight=1, minsize=50) #weight is the rate of change

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5) #padx adds horizontal space, paddy vertivale
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=50, pady=50) #adding pp to .pack makes the space int he widget larger



window.mainloop()
"""


"""
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A", fg='white')
label1.grid(row=0, column=0)


label2 = tk.Label(text="B", fg='white')
label2.grid(row=1, column=0)

#"n" or "N" to align to the top-center part of the cell
#"e" or "E" to align to the right-center side of the cell
#"s" or "S" to align to the bottom-center part of the cell
#"w" or "W" to align to the left-center side of the cell


window.mainloop()
"""






#Address form Example
""""
# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# List of field labels
labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

# Loop over the list of field labels
for idx, text in enumerate(labels):
    # Create a Label widget with the text from the labels list
    label = tk.Label(master=frm_form, text=text)
    # Create an Entry widget
    entry = tk.Entry(master=frm_form, width=50)
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the row whose index is idx
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Start the application
window.mainloop()
"""








#Events and intractions
"""

window = tk.Tk()
window.title('Events')

events = []

# Create an event handler
def keyfuntion(event):

    print(event.char)

window.bind('<key>', keyfuntion())
#.bind() always takes at least two arguments:
#An event that’s represented by a string of the form "<event_name>", where event_name can be any of Tkinter’s events
#An event handler that’s the name of the function to be called whenever the event occurs
#The event handler is bound to the widget on which .bind() is called.
#When the event handler is called, the event object is passed to the event handler function.
def buttonfunction(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", buttonfunction())
#you can bind an event handler to any widget in your application. For example


def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

window.mainloop()
"""





"""
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)



btn_decrease = tk.Button(master=window, text="-", command=decrease())
btn_decrease.grid(row=0, column=0, sticky="nsew")

bl_value = tk.Label(master=window, text="0")
bl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase())
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()

#Label widgets don’t have .get() like Entry and Text widgets do. However, you can retrieve the text from the label by accessing the text attribute with a dictionary-style subscript notation:
"""





#Dice Roll Example
"""
import random
def roll():
    roll_number['text'] = str(random.randint(1,6))

window = tk.Tk()

events = []

window.rowconfigure([0,1,2], minsize=50)
window.columnconfigure([0,1,2], minsize=50)
window.title('Dice')

tk.Label(text='Roll The Dice').grid(row=0, column=1)
roll_button = tk.Button(text="Roll", bg='white', command = roll)
roll_button.grid(row=1, column=1)
roll_number = tk.Label()
roll_number.grid(row=2, column=1)
window.mainloop()
#remember to have .grid/.pack on seperate lines if you need to use the widget

"""







#Text Editor Example Personal Attemept (fail)
"""
from tkinter.filedialog import askopenfilename, asksaveasfilename #V IMPORTANT
def open_file():
    filepath = askopenfilename(
        filetypes=[('Test Files','*.txt'), ('All Files', "*.*")]
    )

    if not filepath:
        return
    txt_edit.delete('1.0', tk.END)
    with open(filepath, mode='r',encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    #Save the current file as a new file.
    filepath = asksaveasfilename(
        #defaultextension=".txt",
        #filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
       return
    with open(filepath, #mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


window = tk.Tk()
window.title('Text Editor')

window.rowconfigure(0, min=800, weight=1)
#The first argument is 0, which sets the height of the first row to 800 pixels
window.columnconfigure(1, min=800, weight=1)
#ow and column indices are zero-based, so these settings apply only to the second column.

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons,text="Open", command=open_file()) #cant have () after command
btn_save = tk.Button(frm_buttons,text="Save", command=save_file())

btn_open.grid(row=0, column=0, sticky="ew",padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew",padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()

"""

#Text Edit Example
""""

from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    #Open a file for editing.
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    #Save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
"""


#Converter Example Personal Attempt
"""
def fahrenheit_to_celsius():
    fahrenheit = ent_temp.get()
    celcius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_results["text"] = f"{round(celcius, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()
window.title('Temperature Converter')
window.resizable(width=False, height=False)

#window.rowconfigure(0, min=100)
#window.columnconfigure(2, min=100)

frm_entry = tk.Frame(master=window)
ent_temp = tk.Entry(master=frm_entry, width=5)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(
    master=window,
    text='\N{RIGHTWARDS BLACK ARROW}',
    command=fahrenheit_to_celsius
)
lbl_results = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_results.grid(row=0, column=2, padx=10)

window.mainloop()
"""

"""
#Converter Example
import tkinter as tk

def fahrenheit_to_celsius():

    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
"""




#Tabs
"""
from tkinter import ttk
def hide():
    notebook.hide(1) #tabs are arranged like lists 0,1 2

def show():
    notebook.add(frame_2, text="tab 2") #use the same that we use to create it

def select():
    notebook.select(1)

window = tk.Tk()
window.title('Tabs')

notebook = ttk.Notebook(window)
notebook.pack()

frame_1 = tk.Frame(bg="White", width=500, height=500)
frame_2 = tk.Frame(bg="Red", width=500, height=500)

frame_1.pack(fill="both", expand=1)
frame_2.pack(fill="both", expand=1)

notebook.add(frame_1, text="tab 1")
notebook.add(frame_2, text="tab 2")

button_1 = tk.Button(frame_1, text="hide 2", command=hide)
button_1.pack()

button_2 = tk.Button(frame_1, text="show 2", command=show)
button_2.pack()

#Navigate to a tab
button_3 = tk.Button(frame_1, text="navigate to 2", command=select)
button_3.pack()


window.mainloop()
"""



"""

from tkinter import ttk

def select():
    notebook.select(1)

def select2():
    notebook.select(0)

window = tk.Tk()
window.title('Tabs')

notebook = ttk.Notebook(window)
notebook.pack()

frame_1 = tk.Frame(bg="White", width=500, height=500)

frame_2 = tk.Frame(bg="Red", width=500, height=500)

frame_1.pack(fill="both", expand=1)
frame_2.pack(fill="both", expand=1)

notebook.add(frame_1)
notebook.add(frame_2)



#Navigate to a tab
button_3 = tk.Button(frame_1, text="navigate to 2", command=select)
button_3.pack()

button_3 = tk.Button(frame_2, text="navigate to 1", command=select2)
button_3.pack()

window.mainloop()

"""



#Animation
"""
import time

# width of the animation window
animation_window_width = 800
# height of the animation window
animation_window_height = 600
# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 30
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.01


# The main window of the animation
def create_animation_window():
    window = tk.Tk()
    window.title("Tkinter Animation Demo")
    # Uses python 3.6+ string interpolation
    window.geometry(f'{animation_window_width}x{animation_window_height}')
    return window


# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
    canvas = tk.Canvas(window)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas


# Create and animate ball in an infinite loop
def animate_ball(window, canvas, xinc, yinc):
    ball = canvas.create_oval(animation_ball_start_xpos - animation_ball_radius,
                              animation_ball_start_ypos - animation_ball_radius,
                              animation_ball_start_xpos + animation_ball_radius,
                              animation_ball_start_ypos + animation_ball_radius,
                              fill="blue", outline="white", width=4)
    while True:
        canvas.move(ball, xinc, yinc)
        window.update()
        time.sleep(animation_refresh_seconds)
        ball_pos = canvas.coords(ball)
        # unpack array to variables
        xl, yl, xr, yr = ball_pos
        if xl < abs(xinc) or xr > animation_window_width - abs(xinc):
            xinc = -xinc
        if yl < abs(yinc) or yr > animation_window_height - abs(yinc):
            yinc = -yinc


# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_ball(animation_window, animation_canvas, animation_ball_min_movement, animation_ball_min_movement)

"""
import csv
weekly_expenses = 100
ExpenseList = []
#ADD  Opening animation
#ADD FEATURE SO FIRST TIME USERS ENTER INFO BUT AFTER IT LOADS ALL DATA



def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()

def paycheck_entry_get():
    global str_pay
    get = paycheckentry.get()



    paycheck_x_expenses = float(get) - weekly_expenses
    str_pay = ""
    # Have money plus savings
    if paycheck_x_expenses > weekly_expenses:


        paycheck_final = paycheck_x_expenses - 20
        str_pay = str("Your Total Spending amount is: " + "$" + str(round(paycheck_final, 2)) +'\n')
        Daily_limit = float(paycheck_final) / 8  # using 8 to keep extra for next week
        str_pay += str("Daily Limit is: " + "$" + str(round(Daily_limit, 2)) + '\n'+
        "Take out $20 for Savings"
        )

    # Has Money but too little for savings
    if paycheck_x_expenses <= weekly_expenses and paycheck_x_expenses > 0:
        str_pay = str("Your Total Spending amount is: " + "$" + str(round(paycheck_x_expenses, 2)) + "\n")
        Daily_limit = float(paycheck_x_expenses) / 8
        str_pay += "Daily Limit is: " + "$" + str(round(Daily_limit, 2)) + "\n"
        str_pay += "Too little to Add to Savings. Keep All Money for Spending this Week"
    # Made no money
    if paycheck_x_expenses == 0:
        str_pay = "You Have $0 for this week" + "\n"
        str_pay += "Do not spend more than $2 a day"
    # Lost money
    if paycheck_x_expenses < 0:
        str_pay = "You are " + "$" + str(round(paycheck_x_expenses, 2)) + " BEHIND!" + "\n"
        str_pay += "Do not spend more than $2 a day"
    Week_Analysis()


def paycheck():
    global Home_page_frame
    global Paycheck_page_frame
    clear(Home_page_frame)
    Paycheck_page_frame = tk.Frame()
    Paycheck_page_frame.grid(row=0, column=0)
    Fi_py = tk.Label(master=Paycheck_page_frame, text='FI.Py', bg='Orange', width=50, height=3)
    Fi_py.grid(row=0, column=1)
    space = tk.Label(master=Paycheck_page_frame, text=' ', bg='White', width=20, height=3)
    space.grid(row=0, column=0)
    space_2 = tk.Label(master=Paycheck_page_frame, text=' ', bg='White', width=20, height=3)
    space_2.grid(row=0, column=2)
    global paycheckentry
    paycheckentry = tk.Entry(master=Paycheck_page_frame, text="Paycheck Amount", width=46)
    paycheckentry.grid(row=2, column=1)
    dollar_sign = tk.Label(master=Paycheck_page_frame, text= "\N{DOLLAR SIGN}")
    dollar_sign.grid(row=2, column=1, sticky= "w")
    Enter_button = tk.Button(master=Paycheck_page_frame, text="Enter", command=paycheck_entry_get)
    Enter_button.grid(row=3, column=1)
    Enter_pay = tk.Label(master=Paycheck_page_frame, text='How Much Were You Paid This Week?')
    Enter_pay.grid(row=1, column=1)
    back = tk.Button(master=Paycheck_page_frame, text="Back", command=back_paycheck)
    back.grid(row=4, column=1)


def back_New_Expense_list_Frame():

    global Expense_list_Frame
    global New_Expense_list_Frame
    clear(New_Expense_list_Frame)
    manage_expenses()
    #BUG WITH BACK BUTTON



def New_Expense_List():
    clear(Manage_page_frame)
    global New_Expense_list_Frame
    global back_New_Expense_list_Frame
    New_Expense_list_Frame = tk.Frame()
    New_Expense_list_Frame.grid(row=0, column=0)
    Fi_py = tk.Label(master=New_Expense_list_Frame, text='FI.Py', bg='Orange', width=50, height=3)
    Fi_py.grid(row=0, column=1)
    space = tk.Label(master=New_Expense_list_Frame, text=' ', bg='White', width=20, height=3)
    space.grid(row=0, column=0)
    space_2 = tk.Label(master=New_Expense_list_Frame, text=' ', bg='White', width=20, height=3)
    space_2.grid(row=0, column=2)

    back_New_Expense_list_Frame = tk.Button(master=New_Expense_list_Frame, text='Back', command=back_New_Expense_list_Frame)
    back_New_Expense_list_Frame.grid(row=2, column=1)


def back_chart_button():
    global Chart_frame
    clear(Chart_frame)
    manage_expenses()


def Chart_list():
    clear(Manage_page_frame)
    global Chart_frame
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
        expense_name = tk.Label(master=Chart_frame, text=str(expense_name))
        expense_name.grid(row=i + 1, column=0)

        price = ExpenseList[i][1]
        price = tk.Label(master=Chart_frame, text=str(price))
        price.grid(row=i + 1, column=1)

        w_m = ExpenseList[i][2]
        w_m = tk.Label(master=Chart_frame, text=str(w_m))
        w_m.grid(row=i + 1, column=2)

    list_len = len(ExpenseList)

    button = tk.Button(master=Chart_frame, text="Add Expense")
    button.grid(row=(list_len + 2), column=1)

    button_2 = tk.Button(master=Chart_frame, text="Edit Expense")
    button_2.grid(row=(list_len + 3), column=1)

    button_3 = tk.Button(master=Chart_frame, text="Back", command=back_chart_button)
    button_3.grid(row=(list_len + 4), column=1)



def manage_expenses():
    global Home_page_frame
    clear(Home_page_frame)
    global Manage_page_frame
    global Expense_list
    global Chart_frame
    Manage_page_frame = tk.Frame()
    Manage_page_frame.grid(row=0, column=0)
    Fi_py = tk.Label(master=Manage_page_frame, text='FI.Py', bg='Orange', width=50, height=3)
    Fi_py.grid(row=0, column=1)
    space = tk.Label(master=Manage_page_frame, text=' ', bg='White', width=20, height=3)
    space.grid(row=0, column=0)
    space_2 = tk.Label(master=Manage_page_frame, text=' ', bg='White', width=20, height=3)
    space_2.grid(row=0, column=2)

    read = tk.Button(master=Manage_page_frame, text="Open Expense List", command=Chart_list)
    read.grid(row=1, column=1)
    New_list = tk.Button(master=Manage_page_frame, text="Make a New Expense List", command=New_Expense_List)
    New_list.grid(row=2, column=1)
    add_expense = tk.Button(master=Manage_page_frame, text="Add Expense")
    add_expense.grid(row=3, column=1)
    edit_expense = tk.Button(master=Manage_page_frame, text="Edit Expenses")
    edit_expense.grid(row=4, column=1)
    back = tk.Button(master=Manage_page_frame, text="Back", command=back_manage)
    back.grid(row=5, column=1)

    global current_window

def back_anaylsis():
    clear(Week_Analysis_page_frame)
    paycheck()



def Week_Analysis():
    global Week_Analysis_frame
    global str_pay
    clear(Paycheck_page_frame)
    global Week_Analysis_page_frame
    Week_Analysis_page_frame = tk.Frame()
    Week_Analysis_page_frame.grid(row=0, column=0)
    Fi_py = tk.Label(master=Week_Analysis_page_frame, text='FI.Py', bg='Orange', width=50, height=3)
    Fi_py.grid(row=0, column=1)
    space = tk.Label(master=Week_Analysis_page_frame, text=' ', bg='White', width=20, height=3)
    space.grid(row=0, column=0)
    space_2 = tk.Label(master=Week_Analysis_page_frame, text=' ', bg='White', width=20, height=3)
    space_2.grid(row=0, column=2)
    analysis = tk.Label(master=Week_Analysis_page_frame, text=str_pay)
    analysis.grid(row=1, column=1)
    back_paycheck = tk.Button(master=Week_Analysis_page_frame, text='back', command=back_anaylsis)
    back_paycheck.grid(row=2, column=1)





def quit_program():
    window.quit()

def back_paycheck():
    clear(Paycheck_page_frame)
    homepage()

def back_manage():
    clear(Manage_page_frame)
    homepage()


def homepage():
    global Home_page_frame
    Home_page_frame = tk.Frame()
    clear(Home_page_frame)
    Home_page_frame.grid(row=0, column=0)


    Fi_py = tk.Label(master=Home_page_frame, text='FI.Py', bg='Orange', width=50, height=3)
    Fi_py.grid(row=0, column=1)
    space = tk.Label(master=Home_page_frame, text=' ', bg='White', width=20, height=3)
    space.grid(row=0, column=0)
    space_2 = tk.Label(master=Home_page_frame, text=' ', bg='White', width=20, height=3)
    space_2.grid(row=0, column=2)

    Paycheck = tk.Button(master=Home_page_frame, text="Paycheck", command=paycheck)
    Paycheck.grid(row=1, column=1)
    Expenses = tk.Button(master=Home_page_frame, text="Manage Expenses", command=manage_expenses)
    Expenses.grid(row=2, column=1)
    quit = tk.Button(master=Home_page_frame, text="Quit", command=quit_program)
    quit.grid(row=3, column=1)


window = tk.Tk()
window.title('Fi.Py')

window.rowconfigure(0, min=50, weight=2)
window.columnconfigure(0, min=50, weight=2)


homepage()




window.mainloop()






