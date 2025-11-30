# Personal Finance Manager

## Video demo: https://youtu.be/7HuMXXVhJIM

## Project Description

This project is a command-line Python application designed to help users manage their personal finances. It allows users to record expenses with details such as amount, category, description, and date. The program supports various reporting features including viewing total expenses, filtering by category or date range, generating monthly summaries, identifying top spending categories, and visualizing data with text-based charts.
In addition to its core functionality, the project includes automated unit tests written with `pytest` to ensure reliability and correctness. The code is modular, with multiple top-level functions handling different aspects of the application logic. All data is stored in a JSON file for persistence.
This project was developed as part of the CS50P final assignment and demonstrates practical use of Python features such as file I/O, data structures, error handling, and testing.

## Features:
- Add new expenses with category, description, and date
- View total expenses
- View expenses by category
- View expenses by date range
- View all expenses
- Monthly summary (total and average per day)
- Top categories (highest spending categories)
- Text chart of expenses
- Search expenses by description
- sort expenses (by date or amount)

## Usage:
1. Clone or download the project.
2. Run the program:
''''bash
python project.py

## Sample output:
Personal Finance Manager
Menu:
1. Add Expense
2. View all Expenses
3. View total Expenses
...
Choose an option: 1
Enter amount (Toman): ...
Enter category: ...
Description: ...
Enter date (YYYY-MM-DD): ...
Expense added successfully.
Press Enter to return to menu

## Tests:
Automated tests are included to validate the main features.
Run the following command to execute all tests:
pytest test_project.py

## The tests cover:
Adding expense and calculating totals
Filtering by category and date range
Monthly summary calculations
Top categories
Searching by description
Sorting expenses

## project structure:
project.py > Main application code
test_project.py > Unit tests
expenses.json > Data file sorting expenses
README.md > Project documentation
