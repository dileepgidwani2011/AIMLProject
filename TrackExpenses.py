from datetime import datetime

import pandas as pd
import os

expenses =  []
fileName = "expenses5.csv"
maxMenuRetry = 3
state = {"needSave": False, "monthlyBudget": 30.0}
loadedExpenses = []

def menu():
    ''' This function shows the menu to user'''

    userOption = -1;
    retry = 1

    loadExpenses()

    while (userOption >= 1 and userOption <= 6) or retry <= maxMenuRetry :
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Set monthly Budget")
        print("6. Exit")

        userOption = int(input("Please select an option:"))

        if userOption == 1:
            addExpense()
        elif userOption == 2:
            viewExpenses()
        elif userOption == 3:
            trackBudget()
        elif userOption == 4:
            saveExpenses()
        elif userOption == 5:
            setBudget()
        elif userOption == 6:
            endProcess()
        else:
            print("Invalid Option")
            retry = retry + 1
            continue
        retry = 1
    else:
        print("Max retry reached!")



def loadExpenses():
    loadedExpenses.clear()
    try:
        existingexpenses = pd.read_csv(fileName).to_dict(orient="records")
        for expense in existingexpenses:
            loadedExpenses.append(expense)
    except FileNotFoundError:
        print("There are no existing expenses to load!")


def endProcess():
    if state["needSave"]:
        wanttosave = input("You have some expenses to be saved, Do you want to save them before exit(y/n)?")
        if wanttosave == "y":
            saveExpenses()
            exit()
    exit()


def get_date():
    ''' This function returns the date of the expense '''

    retry = 1
    while retry <= 3:
        date_str = input("Please enter the date of expense(YYYY-MM-DD): ")
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            print("Valid date:", date_obj.date())
            return date_obj.date()
        except ValueError:
            retry += 1
            print("Invalid format! Please enter the date in YYYY-MM-DD format.")
    raise ValueError("Invalid date format, max retries exceeded.")

def addExpense():
    ''' This function adds a new expense '''

    expenseDate= get_date()
    expenseCategory= input("Please enter the category of expense(Like Food or Travel):")
    expenseAmount= float(input("Please enter the amount of expense:"))
    expenseDescription = input("Please enter the description of expense:")

    expense = {"date": expenseDate, "category": expenseCategory.lower(), "amount": expenseAmount, "description": expenseDescription}
    expenses.append(expense)

    state["needSave"] = True
    print("Expenses added successfully!!")


def viewExpenses():
    ''' This function shows the expenses '''
    for expense in expenses:
        isExpenseValid = isValid(expense)
        if isExpenseValid:
            print(expense)

    for expense in loadedExpenses:
        isExpenseValid = isValid(expense)
        if isExpenseValid:
            print(expense)

def isValid(expense):
    ''' This function checks if the expense is valid'''

    return (
            expense.get('amount') not in [None, ""]
            and expense.get('category') not in [None, ""]
            and expense.get('description') not in [None, ""]
            and expense.get('date') not in [None, ""]
    )

def saveExpenses():
    ''' This function saves the expenses '''
    df = pd.DataFrame(expenses)

    # Check if the file exists
    file_exists = os.path.isfile(fileName)

    # Append if file exists, otherwise create a new file
    df.to_csv(fileName, mode='a', header=not file_exists, index=False)
    print(f"Data saved to {fileName}")
    state["needSave"] = False
    expenses.clear()
    loadExpenses()


def setBudget():
    ''' This function sets the budget for each expense '''

    state["monthlyBudget"] = float(input("Please enter the monthly budget:"))


def trackBudget():
    ''' This function tracks the budget'''

    existingExpensesAmount = 0.0
    for expense in expenses:
        existingExpensesAmount += float(expense.get('amount'))

    for expense in loadedExpenses:
        existingExpensesAmount += float(expense.get('amount'))

    if (existingExpensesAmount > state["monthlyBudget"]):
        print("You have exceeded your budget!")
    else:
        print(f"""You have {state["monthlyBudget"]-existingExpensesAmount} left for the month!""")


menu()



