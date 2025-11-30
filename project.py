import json
from datetime import datetime

DATA_FILE = 'expenses.json'

def main():
    print("\nPersonal Finance Manager")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View total Expenses")
        print("4. View Expenses by category")
        print("5. View Expenses by date range")
        print("6. Monthly summary")
        print("7. Top Categories")
        print("8. Text Chart of Expenses")
        print("9. Search Expenses by description")
        print("10. Sort Expenses")
        print("11. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            handle_add_expense()
        elif choice == '3':
            print(f"Total Expenses: {get_total_expenses()} Toman")
            input("Press Enter to return to menu")
        elif choice == '4':
            category = input("Enter category: ")
            print(f"Total for '{category}': {get_expenses_by_category(category)} Toman")
            input("Press Enter to return to menu")
        elif choice == '5':
            print("Tip: If you want to see expenses for a single day, enter the same date for start and end.")
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            filtered = get_expenses_by_date_range(start, end)
            print("\nFiltered Expenses:")
            for exp in filtered:
                print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            input("\nPress Enter to return to menu")
        elif choice == '2':
            expenses = load_data()
            if not expenses:
                print("No expenses recorded.")
            else:
                print("\nAll Expenses:")
                for exp in expenses:
                    print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            input("\nPress Enter to return to menu")
        elif choice == '6':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            summary = get_monthly_expenses(year, month)
            print(f"\nMonthly Summary for {year}-{month}:")
            print(f"Total: {summary['total']} Toman")
            print(f"Average per day: {summary['average_per_day']:.2f} Toman")
            input("\nPress Enter to return to menu")
        elif choice == '7':
            top = get_top_categories()
            print("\nTop Categories:")
            for cat, total in top:
                print(f"{cat}: {total} Toman")
            input("\nPress Enter to return to menu")
        elif choice == '8':
            render_text_chart()
            input("\nPress Enter to return to menu")
        elif choice == '9':
            keyword = input("Enter keyword to search in descriptions: ")
            results = search_by_description(keyword)
            print("\nSearch Results:")
            for exp in results:
                print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            input("\nPress Enter to return to menu")
        elif choice == '10':
            mode = input("Sort by 'date' or 'amount': ").lower()
            sorted_expenses = sort_expenses(mode)
            print("\nSorted Expenses:")
            for exp in sorted_expenses:
                print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
            input("\nPress Enter to return to menu")
        elif choice == '11':
            print("Goodbye")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to return to menu")
def handle_add_expense():
    try:
        amount = int(input("Enter amount (Toman): "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        category = input("Enter category: ")
        description = input("Description: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        datetime.strptime(date_str, "%Y-%m-%d")
        add_expense(amount, category, description, date_str)
        print("\nExpense added successfully.")
        input("\nPress Enter to return to menu")
    except ValueError as e:
        print(f"Error: {e}")
def add_expense(amount, category, description, date_str):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date_str
    }
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(expense)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
def get_total_expenses():
    data = load_data()
    return sum(e["amount"] for e in data)
def get_expenses_by_category(category):
    data = load_data()
    return sum(e["amount"] for e in data if e["category"].lower() == category.lower())
def get_expenses_by_date_range(start, end):
    data = load_data()
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()
    return [e for e in data if start_date <= datetime.strptime(e["date"], "%Y-%m-%d").date() <= end_date]
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def get_monthly_expenses(year, month):
    data = load_data()
    monthly = [e for e in data if datetime.strptime(e["date"], "%Y-%m-%d").month == month and datetime.strptime(e["date"], "%Y-%m-%d").year == year]
    total = sum(e["amount"] for e in monthly)
    avg = total / len(set(e["date"] for e in monthly)) if monthly else 0
    return {"total": total, "average_per_day": avg}
def get_top_categories(n=3):
    data = load_data()
    categories= {}
    for e in data:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    return sorted_categories[:n]
def render_text_chart():
    data = load_data()
    categories = {}
    for e in data:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    print("\nExpenses Chart:")
    for cat, total in categories.items():
        print(f"{cat:12}: {'#'*(total // 1000)}")
def search_by_description(keyword):
    data = load_data()
    return [e for e in data if keyword.lower() in e["description"].lower()]
def sort_expenses(mode):
    data = load_data()
    if mode == "date":
        return sorted(data, key=lambda e: datetime.strptime(e["date"], "%Y-%m-%d"))
    elif mode == "amount":
        return sorted(data, key=lambda e: e["amount"], reverse=True)
    else:
        print("Invalid sort mode. Use 'date' or 'amount'.")
        return data

if __name__ == "__main__":
    main()

