import datetime
import os
def add_diary_entry():
    """
    Adds a new entry to the diary with the current date and time.
    """
    data=input("Enter the entry: ")
    with open('diary.txt','a') as diary:
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        diary.write(f"{date} : {data}\n")
    print("Diary entry added successfully.")

def read_diary_entries():
    """
    Reads and displays diary entries from a specific date.
    """
    if os.path.exists('diary.txt'):
        date=input("Enter the date (YYYY-MM-DD): ")
        with open('diary.txt','r') as diary:
            for line in diary:
                if date in line:
                    print(line.strip())
    else:
        print("No diart entries not found.")

def main():
    """
    The main function to run the Personal Diary Application.
    """
    while True:
        print("\nPersonal Diary Application")
        print("1. Add a new diary entry")
        print("2. Read diary entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        if choice == "1":
            add_diary_entry()
        elif choice == "2":
            read_diary_entries()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()