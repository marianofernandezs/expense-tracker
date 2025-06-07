import os #Imporing os to navigate between folders
import json
from datetime import datetime

def add_expense(description: str, category: str, amount: float, date: str):

    data_path = os.path.join(os.path.dirname(__file__), 'data', 'expenses.json')

    if not os.path.exists(data_path):
        expenses = []
    else:
        with open(data_path, 'r') as file:
            expenses = json.load(file)
    if len(description) == 0:
        raise ValueError("Description must not be empty")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if len(category) == 0 or category.isnumeric():
        raise ValueError("Category is empty or is numeric")

    datetime.strptime(date, "%Y-%m-%d")

    id = len(expenses) + 1
    expense = {
        "id": id,
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    with open(data_path, 'w') as file:
        json.dump(expenses, file, indent=4)

    return expense
