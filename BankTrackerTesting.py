import csv
import pyinputplus as pyip

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
        print('Enter -1 to Cancel')
        logdate = input('Date\n')
        if logdate == '-1':
            break
        bal = pyip.inputFloat('Checking Balance\n$')
        if bal == -1:
            break
        loglist.append([logdate, bal])
        printloglist()
        break

    Savebal = input('Would You Like to Save Balance to Log And Calculate Profit? (Y/N)\n')

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
        print('Enter -1 to Cancel')
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
        print('Enter -1 to Cancel')
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



#Menu
while True:
    MainMenuOption = pyip.inputInt('(1) Test1\n(2) Manage Balance\n', min=1, max=2)
    if MainMenuOption == 1:
        print('test')
    if MainMenuOption == 2:
            BalanceMenu_choice = pyip.inputInt(prompt='(1) Add Balance\n(2) Edit Balance Log\n', min=1, max=2)
            #Add Balance
            if BalanceMenu_choice == 1:
                log()
            #Edit Balance Log
            if BalanceMenu_choice == 2:
                append_to_loglist()
                printloglist()

                editlog_options_choice = pyip.inputInt(prompt='(1) Edit A Balance\n(2) Delete A Balance\n', min=1, max=2)
                # Edit A Balance
                if editlog_options_choice == 1:
                    loglist.clear()
                    editlog()
                    break
                # Delete A Balance
                if editlog_options_choice == 1:
                    loglist.clear()
                    deletelog()
                    break





"""
read log(edit log), add balance 
its best to add on the same day (after youve been paid)
enter date and balance 
enter checking account balance
retrieve last log
made/loss
save balance to log?
"""

