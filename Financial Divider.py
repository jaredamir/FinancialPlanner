import csv
import pyinputplus as pyip

#NEED TO ROUND UP
#Add last balance pop up when aadding new one (print-1)
#no file failsafe try and exceptions
#adjust for  people with non weekly paydays
#savings section

#Variables
Expense_list = []
NewExpense_list = []




#Functions
loglist = []
def printloglist():
    print('  Date    Balance')
    for i in range(len(loglist)):
        print(loglist[i])

def calc_balance_change():  #used after input and saved to log
    with open('Balance log', 'r') as file:
        logr = csv.reader(file)

        for row in (logr):
            loglist.append(row)

        Bal_change = (float(loglist[-1][1])) - (float(loglist[-2][1]))

        if float(Bal_change) > 0:
            print("You've Made " + "$" + str(Bal_change) +"\nNice Job!")

        if float(Bal_change) < 0:
            print('You LOST ' + "$" + str(Bal_change) + "!\nWe Advise You Spend Carefully")

        if float(Bal_change) == 0:
            print('Balance Unchanged')
    loglist.clear()



def log():
    print('It is Recommended That You Enter Balance After Receiving Paycheck and Taking out Savings')
    while True:
        print('**Enter -1 to Cancel**')
        logdate = input('Date\n')
        if logdate == '-1':
            break
        bal = pyip.inputFloat('Checking Balance\n$')
        if bal == -1:
            break
        loglist.append([logdate, bal])
        printloglist()
        break

    Savebal = input('Would You Like to Save Balance And Calculate Profit? (Y/N)\n')

    if Savebal.capitalize() == 'Y':
        with open('Balance log', 'a') as file:
            logw = csv.writer(file)

            for i in range(len(loglist)):
                logw.writerow(loglist[i])
            loglist.clear()
        calc_balance_change()

    if Savebal.capitalize() == 'N':
        choice1 = print('not saved')#input('(1) Edit Expense\n(2) Add More Expenses\n(3) Delete Current List')
        print('')


def make_new_bal_log():
    while True:
        print('**Enter -1 to Cancel**')
        logdate = input('Date\n')
        if logdate == '-1':
            break
        bal = pyip.inputFloat('Checking Balance\n$')
        if bal == -1:
            break
        loglist.append([logdate, bal])
        printloglist()


    Savebal = pyip.inputYesNo('Would You Like to Save New Balance Log?\n')
    if Savebal == 'yes':
        with open('Balance log', 'w') as  file:
            ballog = csv.writer(file)

            for i in range(len(loglist)):
                ballog.writerow(loglist[i])
        print('Changes Saved. Thank You!\n ')
    if Savebal  == 'no':
        print('Changes Not Saved\n ')




def append_to_loglist():
    with open('Balance log', 'r') as file:
        log = csv.reader(file)

        for row in log:
            loglist.append(row)


def printnumlog():
    append_to_loglist()
    print('    Date    Balance')
    for i in range(len(loglist)):
        print(str(i+1) + ' ' + str(loglist[i]))

def editlog():

    printnumlog()

    i=1
    while i<100000000000:
        print('**Enter -1 to Cancel**')
        editlog_choice = pyip.inputInt(prompt='Which Balance Would You Like to Edit?\n', max=(len(loglist)))
        if editlog_choice == -1:
            print('Canceled')
            break
        if editlog_choice == 0:
            print('Please Choose a number between 1-' + str(len(loglist)) +'\nPlease Retry')

            break

        logdate = input('Date\n')
        if logdate == '-1':
            print('Canceled')
            break
        bal = pyip.inputFloat('Checking Balance\n$')
        if bal == float(-1):
            print('Canceled')
            break
        loglist[((editlog_choice)-1)] = [logdate, bal]

        print('    Date    Balance')
        for i in range(len(loglist)):
            print(str(i + 1) + ' ' + str(loglist[i]))

        editagain = pyip.inputYesNo('Would You Like To Edit Another? (Yes or No)\n')
        if editagain == 'yes':
            i=1
        if editagain == 'no':
            break

    saveeditlog = pyip.inputYesNo('Would You Like to Save Changes? (Yes or No)\n')
    if saveeditlog == 'yes':
        with open('Balance log', 'w') as file:
            logw = csv.writer(file)

            for i in range(len(loglist)):
                logw.writerow(loglist[i])
        print('Changed Saved. Thank You!\n ')
        loglist.clear()
    if saveeditlog == 'no':
        print('Changes Not Saved\n  ')
        loglist.clear()


def deletelog():
    printnumlog()
    i = 1
    while i < 100000000000:
        print('**Enter -1 to Cancel**')
        deletelog_choice = pyip.inputInt(prompt='Which Balance Would You Like to Delete?\n', max=(len(loglist)))
        if deletelog_choice == -1:
            print('Canceled')
            break
        if deletelog_choice == 0:
            print('Please Choose a number between 1-' + str(len(loglist)) + '\nPlease Retry')
            break

        del loglist[(deletelog_choice)-1]

        print('    Date    Balance')
        for i in range(len(loglist)):
            print(str(i + 1) + ' ' + str(loglist[i]))

        deleteagain = pyip.inputYesNo('Would You Like To Delete Another? (Yes or No)\n')
        if deleteagain == 'yes':
            i = 1

        if deleteagain == 'no':
            break

    saveeditlog = pyip.inputYesNo('Would You Like to Save Changes? (Yes or No)\n')
    if saveeditlog == 'yes':
        with open('Balance log', 'w') as file:
            logw = csv.writer(file)

            for i in range(len(loglist)):
                logw.writerow(loglist[i])
        print('Changed Saved. Thank You!\n ')
        loglist.clear()
    if saveeditlog == 'no':
        print('Changes Not Saved\n  ')
        loglist.clear()


def printexpenses():
    with open('Expenses V2.csv', 'r') as file:
        exfile = csv.reader(file)

        print('Expense ' + ' Price')
        for row in exfile:
            print(row)


def append_to_list():
    with open('Expenses V2.csv', 'r') as file:
        exfile = csv.reader(file)

        for row in exfile:
            Expense_list.append(row)

def append_to_newlist():
    with open('Expenses V2.csv', 'r') as file:
        exfile = csv.reader(file)

        for row in exfile:
            NewExpense_list.append(row)

def printnumexpenses():
    print('   ' + 'Expense ' + ' Price')
    for i in range(len(NewExpense_list)):
        print(str(i + 1) + ' ' + str(NewExpense_list[i]))

def calculate_weekly_expenses():
    with open('Expenses V2.csv', 'r') as file:
        exfile = csv.reader(file)

    append_to_list()
    global weekly_expenses
    weekly_expenses = 0
    for i in range(len(Expense_list)):
        weekly_expenses += float(Expense_list[i][1])



def printlist():
    print('Expense ' + ' Price')
    for i in range(len(Expense_list)):
        print(Expense_list[i])

def printnewlist():
    print('Expense ' + ' Price')
    for i in range(len(NewExpense_list)):
        print(NewExpense_list[i])



def new_expenses():
    while True:
        print('Press Enter with an Empty Input to Finish')
        exname = input('Expense Name?\n')

        if exname == '':
            break

        WoE = input('Is this a weekly or monthly expense?(M/W)\n')
        if WoE == '':
            break
        price = input('Price?\n$')
        if price == '':
            break

        if WoE.upper() == 'M':  # and price == float:
            price = (float(price)) / 4
            NewExpense_list.append([exname, price])
            printnewlist()

        elif WoE.capitalize() == 'W':  # and price == float:
            pass
            NewExpense_list.append([exname, price])
            printnewlist()

        else:
            print('Re-enter Expense, Please put M or W and a valid number for price')

    printnewlist()
    Save = input('Would you like to save new sheet? (Y/N)\n')
    if Save.capitalize() == 'Y':
        with open('Expenses V2.csv', 'w') as file:
            Expenses = csv.writer(file)

            for i in range(len(NewExpense_list)):
                Expenses.writerow(NewExpense_list[i])
        NewExpense_list.clear()
        print('New List Saved! Thank You')

    elif Save.capitalize() == 'N':
        print('Changes Not Saved\n ')







calculate_weekly_expenses()

#Main Menu
print('FINACIAL PLANNER')

i = 1
while True:
    MainMenuOption = input('(1) Enter Paycheck\n(2) Manage Balance\n(3) Manage Expenses\n(4) Quit Finacial Planner\n')
    if MainMenuOption == '1':
        #Calculating Expenses
        with open('Expenses V2.csv', 'r') as file:
            exfile = csv.reader(file)

        append_to_list()
        global weekly_expenses
        weekly_expenses = 0
        for i in range(len(Expense_list)):
            weekly_expenses += float(Expense_list[i][1])
        i = 1
        while i < 10000000000:
#Paycheck
            paycheck = pyip.inputFloat("(Enter -1 to Return to Main Menu)\n" + "Paycheck\n")
            if paycheck == -1:
                break
            #elif float(paycheck) != float:
                #print('Please Enter a Number')  #***FIXX**
            else:
            #calculate_weekly_expenses()
                paycheck_x_expenses = float(paycheck) - weekly_expenses
            #Have money plus savings
                if paycheck_x_expenses > weekly_expenses:
                    paycheck_final = paycheck_x_expenses - 20
                    print("Your Total Spending amount is: " + "$" + str(round(paycheck_final, 2)))
                    Daily_limit = float(paycheck_final)/8 #using 8 to keep extra for next week
                    print("Daily Limit is: " + "$" + str(round(Daily_limit, 2)))
                    print("Take out $20 for Savings")
                #Has Money but too little for savings
                if paycheck_x_expenses <= weekly_expenses and paycheck_x_expenses > 0:
                    print("Your Total Spending amount is: " + "$" + str(round(paycheck_x_expenses,2)))
                    Daily_limit = float(paycheck_x_expenses)/ 8
                    print("Daily Limit is: " + "$" + str(round(Daily_limit, 2)))
                    print("Too little to Add to Savings. Keep All Money for Spending this Week")
                #Made no money
                if paycheck_x_expenses == 0:
                    print("You Have $0 for this week")
                    print("Do not spend more than $2 a day")
                #Lost money
                if paycheck_x_expenses < 0:
                    print("You are " + "$" + str(round(paycheck_x_expenses, 2)) + " BEHIND!")
                    print("Do not spend more than $2 a day")
            print('Make Sure to Update Balance Log')
            print(" ")

#Manage Balance
    elif MainMenuOption == "2":
        while True:
            BalanceMenu_choice = pyip.inputInt(prompt='(1) Add Balance\n(2) Make New Balance log\n(3) Edit Balance Log\n(4) Return To Main Menu\n', min=1, max=4)
            #Add Balance
            if BalanceMenu_choice == 1:
                log()

            if BalanceMenu_choice == 2:
                make_new_bal_log()

            #Edit Balance Log
            if BalanceMenu_choice == 3:
                append_to_loglist()
                printloglist()


                # Edit A Balance
                while True:
                    editlog_options_choice = pyip.inputInt(prompt='(1) Edit A Balance\n(2) Delete A Balance\n(3) Back\n', min=1, max=3)
                    if editlog_options_choice == 1:
                        loglist.clear()
                        editlog()


                    # Delete A Balance
                    if editlog_options_choice == 2:
                        loglist.clear()
                        deletelog()


                    if editlog_options_choice == 3:
                        break

           #return to main menu
            if BalanceMenu_choice == 4:
                break
#Manage Expenses
    elif MainMenuOption == '3':
        while i < 1000000:
            ExpMenuOption = input('EXPENSE OPTIONS\n(1) Read Expense List\n(2) Make A New Expense List\n(3) Add Expense\n(4) Edit Expense\n(5) Delete Expense From List\n(6) Return to Main Menu\n')

            if ExpMenuOption == '1':
                # opening Expense File
                printexpenses()

                print('Weekly Expense is ' + str(round(weekly_expenses, 2)))

                input('\nPress Enter to Go Back')
                print(' ')


            elif ExpMenuOption == '2':
                #Making A new List
                new_expenses()



            elif ExpMenuOption == '3':
                # Appending Expense File
                with open('Expenses V2.csv', 'r') as file:
                    exfile = csv.reader(file)

                    for row in exfile:
                        NewExpense_list.append(row)
                printnewlist()
                new_expenses()


            #Edit Expense
            elif ExpMenuOption == '4':
                with open('Expenses V2.csv', 'r') as file:
                    expenses = csv.reader(file)

                    for row in expenses:
                        NewExpense_list.append(row)

                printnumexpenses()

                while True:
                    while True:
                        raweditchoice = input('Which Expense Would You Like to Edit? (Press Enter With Empty Input to Cancel)\n')
                        if raweditchoice == '':
                            break
                        if int(raweditchoice) > (len(NewExpense_list)-1):
                            print('That Expense Is Not On The List, Please Try Again')
                            break
                        if int(raweditchoice) == 0:
                            print('That Expense Is Not On The List, Please Try Again')
                            break
                        editchoice = int(raweditchoice) - 1
                        print('Press Enter with an Empty Input to Finish')
                        exname = input('Expense Name?\n')
                        if exname == '':
                            break

                        WoE = input('Is this a weekly or monthly expense?(M/W)\n')
                        if WoE == '':
                            break

                        price = input('Price?\n')
                        if price == '':
                            break

                        if WoE.upper() == 'M':  # and price == float:
                            price = (float(price)) / 4
                            #NewExpense_list.append([exname, price])
                            NewExpense_list[editchoice] = [exname, price]
                            printnewlist()

                        elif WoE.capitalize() == 'W':  # and price == float:
                            NewExpense_list[editchoice] = [exname, price]
                            printnewlist()

                        else:
                            print('Re-enter Expense, Please put M or W and a valid number for price')

                        edit_another_choice = pyip.inputYesNo('Edit Another (Y/N)\n')
                        if edit_another_choice.capitalize() == 'yes':
                            pass
                        if edit_another_choice.capitalize() == 'no':
                            break


                    after_change_choice = input('(1) Save Updated List\n(2) Cancel Changes\n')

                    if after_change_choice == '1':
                        with open('Expenses V2.csv', 'w') as file:
                            Expenses = csv.writer(file)

                            for i in range(len(NewExpense_list)):
                                Expenses.writerow(NewExpense_list[i])
                        NewExpense_list.clear()
                        print('Changes Saved. Thank You!')
                        print(' ')
                        break
                    if after_change_choice == '2':
                        print('Edits Canceled')
                        print(' ')
                        NewExpense_list.clear()
                        break


            #Delete Expense
            elif ExpMenuOption == '5':
                append_to_newlist()
                printnumexpenses()
                while i<10000000:
                    rawdeletechoice = pyip.inputInt(prompt='Which Expense Would You Like to Delete? (**Enter -1 to Cancel**)\n',min=-2, max=(len(NewExpense_list)))
                    if rawdeletechoice == -1:
                        break
                    if rawdeletechoice == 0:
                        print('Please Choose A Number Between 1-' + len(NewExpense_list))

                    deletechoice = int(rawdeletechoice) - 1
                    del NewExpense_list[deletechoice]
                    printnumexpenses()

                    Delete_another_choice = pyip.inputYesNo('Delete Another? (Y/N)\n')
                    if Delete_another_choice.capitalize() == 'yes':
                        i=1
                    if Delete_another_choice.capitalize() == 'no':
                        break

                after_change_choice = input('(1) Save Updated List\n(2) Cancel Changes\n')

                if after_change_choice == '1':
                    with open('Expenses V2.csv', 'w') as file:
                        Expenses = csv.writer(file)

                        for i in range(len(NewExpense_list)):
                            Expenses.writerow(NewExpense_list[i])
                    NewExpense_list.clear()
                    print('Changes Saved. Thank You!')
                    print(' ')
                    break
                if after_change_choice == '2':
                    print('Edits Canceled')
                    print(' ')
                    NewExpense_list.clear()
                    break



            elif ExpMenuOption == '6':
                break

            else:
                print('Please Enter a Number (1-6)')
#Quit
    elif MainMenuOption == '4':
        print('Quiting... Thank You! :)')
        break

    else:
        print('Please Enter a Number (1-4)')




"""
#New Expense List 
with open('Expenses.csv', 'w') as file:
    Expenses = csv.writer(file)
    Expenses.writerow(['Expense', 'Price', 'Weekly or Monthly'])

    numExp = int(input('How Many Expenses Are You Adding?\n'))
    for i in range(numExp):
        Expen = input("Name of Expense\n")
        Price = input("Price without $\n")
        WoE = input("Is This A Weekly or Monthly Expenses?\n")

        Expenses.writerow([Expen, Price, WoE])
"""
"""
#opening Expense File
with open('Expenses.csv','r') as file:
    Expenses = csv.reader(file)

    for row in Expenses:
        print(row)
"""
"""
#Appending Expense File
with open('Expenses.csv', 'r') as file:
    Expenses = csv.reader(file)
    for row in Expenses:
        print(row)
with open('Expenses.csv', 'a+') as file:
    ExpenWrite = csv.writer(file)

    numNewExp = int(input("How Many New Expenses Are You Adding?\n"))
    for i in range(numNewExp):
        Expen = input("Name of Expense\n")
        Price = input("Price without $\n")
        WoE = input("Is This A Weekly or Monthly Expenses?\n")

        ExpenWrite.writerow([Expen, Price, WoE])

with open('Expenses.csv', 'r') as file:
    Expenses = csv.reader(file)
    for row in Expenses:
        print(row)
print('Changes saved')
"""

"""
#Editing an Expense FIXX
List = []
i = 1
editExp = int(input('Which Expense Would You Like to Change?\n'))
for i in range(len(List[0])):
    newExp = input(str(List[0][i]) + '\n')
    List[editExp][i] = newExp

print("New Expense Detais")
for i in range(len(List)):
    print(str(List[i]))
"""






