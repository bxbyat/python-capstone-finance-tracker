print("Welcome to the Personal Finance Tracker!")

tracker = {}


def add_expense(cat: str, des: str, am: str):
    if cat not in tracker:
        tracker[cat] = [(des, am)]
    else:
        tracker[cat].append((des, am))


def view_expenses(data: dict):
    for i in data:
        print("Category: " + i)
        for j in data[i]:
            print(" - " + j[0] + ": $" + j[1])


def view_summary(data: dict):
    print("Summary:")
    for i in data:
        total = 0
        for j in data[i]:
            total += float(j[1])
        print(i + ": $" + str(total))


def menu():
    while True:
        while True:
            choice = input("What would you like to do?\n"
                           "1. Add Expense\n"
                           "2. View All Expenses\n"
                           "3. View Summary\n"
                           "4. Exit\n"
                           "Choose an option: ")
            try:
                test = int(choice) + 1
                if 1 <= int(choice) <= 4:
                    break
                else:
                    print("Please choose a valid choice!")
            except ValueError:
                print("Please choose a valid choice!")
            else:
                break
        if int(choice) == 1:
            while True:
                description = input("Enter expense description: ")
                try:
                    test2 = description + "a"
                    if description != " ":
                        break
                    else:
                        print("Please enter a valid string!")
                except ValueError:
                    print("Please enter a valid string!")
                else:
                    break
            while True:
                category = input("Enter category: ")
                try:
                    test3 = category + "a"
                    if description != " ":
                        break
                    else:
                        print("Please enter a valid string!")
                except ValueError:
                    print("Please enter a valid string!")
                else:
                    break
            while True:
                amount = input("Enter amount: ")
                try:
                    test4 = float(amount) + 1
                except ValueError:
                    print("Please enter a valid number!")
                else:
                    break
            add_expense(category, description, amount)
            print("Expense added successfully.")
        elif int(choice) == 2:
            view_expenses(tracker)
        elif int(choice) == 3:
            view_summary(tracker)
        else:
            break
    print("Goodbye!")


menu()