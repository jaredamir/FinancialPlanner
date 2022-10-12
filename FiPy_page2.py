import csv

Expense_list = []
NewExpense_list = []

def printlist():
    print('Expense ' + ' Price')
    for i in range(len(Expense_list)):
        print(Expense_list[i])

def new_expenses():
    while True:
        exname = input('Expense Name?\n')

        if exname == '':
            break

        WoE = input('Is this a weekly or monthly expense?(M/W)\n')
        if WoE == '':
            break
        price = input('Price?\n')

        if WoE.upper() == 'M':  # and price == float:
            price = (float(price)) / 4
            NewExpense_list.append([exname, price])
            printlist()

        elif WoE.capitalize() == 'W':  # and price == float:
            pass
            NewExpense_list.append([exname, price])
            printlist()

        else:
            print('Re-enter Expense, Please put M or W and a valid number for price')


print('Press Enter With No input to End')
new_expenses()

weekly_expenses = 0
for i in range(len(Expense_list)):
   weekly_expenses += float(Expense_list[i][1])

print(weekly_expenses)

printlist()

Save = input('Would you like to save new sheet? (Y/N)\n')

if Save.capitalize() == 'Y':
    with open('Expenses V2.csv', 'w') as file:
        Expenses = csv.writer(file)
        
        for i in range(len(Expense_list)):
            Expenses.writerow(NewExpense_list[i])
    print('New List Saved! Thank You')
            
elif Save.capitalize() == 'N':
    choice1 = input('(1) Edit Expense\n(2) Add More Expenses\n(3) Delete Current List')
