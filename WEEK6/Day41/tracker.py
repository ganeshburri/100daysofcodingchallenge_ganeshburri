import json
import os
def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    date = input("Enter date of expense (YYYY-MM-DD): ")

    new_expense = {'amount': amount, 'description': description, 'date': date}

    if not os.path.isfile('expenses.json'):
        with open('expenses.json', 'w') as file:
            json.dump([new_expense], file)
    else:
        with open('expenses.json', 'r+') as file:
            expenses = json.load(file)
            expenses.append(new_expense)
            file.seek(0)
            json.dump(expenses, file)


def view_expenses():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        for expense in expenses:
            print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")


def delete_expense():
    view_expenses()
    index = int(input("Enter the index of the expense to delete: "))
    
    with open('expenses.json', 'r+') as file:
        expenses = json.load(file)
        if 0 <= index < len(expenses):
            expenses.pop(index)
            file.seek(0)
            file.truncate()
            json.dump(expenses, file)
        else:
            print("Invalid index.")


def main():
    while True:
        action = input("Choose an action (add, view, delete, exit): ").lower()
        if action == 'add':
            add_expense()
        elif action == 'view':
            view_expenses()
        elif action == 'delete':
            delete_expense()
        elif action == 'exit':
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()