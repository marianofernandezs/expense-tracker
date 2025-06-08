import os # Imporing os to navigate between folders
import json
from datetime import datetime # Importing datetime to transform date a datetime

def add_expense(description: str, category: str, amount: float, date: str):

    data_path = os.path.join(os.path.dirname(__file__), 'data', 'expenses.json') # Searching for expenses.json in data folder

    if not os.path.exists(data_path): # If doesn't exist the expenses.json
        expenses = [] # Create a empty list
    else:
        with open(data_path, 'r') as file: # Opening a file in read mode
            expenses = json.load(file) #
    if len(description) == 0: # Validating if description is empty
        raise ValueError("Description must not be empty")
    if amount <= 0: # Validating if amount is negative or 0
        raise ValueError("Amount must be greater than 0")
    if len(category) == 0 or category.isnumeric(): # Validating if category is null or is a number
        raise ValueError("Category is empty or is numeric")

    datetime.strptime(date, "%Y-%m-%d")

    id = len(expenses) + 1 # Adding the id to the expense
    expense = { # Creating the expense
        "id": id,
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense) # Adding the expense to expenses

    with open(data_path, 'w') as file: # Opening expenses.json in write mode
        json.dump(expenses, file, indent=4)

    return expense # Return the new expense created

def list_expense(filters: dict) -> list[dict]:
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'expenses.json') # Searching for expenses.json in data folder
    if not os.path.exists(data_path):
        return []
    else:
        with open(data_path, 'r') as file: # Opening a file in read mode
            expenses = json.load(file)
    return expenses

def delete_expense(expense_id: int) -> bool:
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'expenses.json') # Searching for expenses.json in data folder
    if not os.path.exists(data_path): # If doesn't exist the expenses.json
        return False
    else:
        with open(data_path, 'r') as file: # Opening a file in read mode
            expenses = json.load(file) #
    new_expenses = [e for e in expenses if e["id"] != expense_id] #e refers to id of the expense and remove the expense matching by id  #check further for more comprehension
    if len(new_expenses) == len(expenses):
        return False # nothing was removed from expenses
    with open(data_path, 'w') as file:
        json.dump(new_expenses,file,indent=4) #we replace the former list expense, with the new information
    return True
