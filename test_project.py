import os
import json
from datetime import datetime
import project

def clear_data():
    if os.path.exists(project.DATA_FILE):
        with open(project.DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
def test_add_and_total_expenses():
    clear_data()
    project.add_expense(10000, "Food", "Pasta", "2025-06-01")
    project.add_expense(20000, "Transport", "Bus ticket", "2025-06-02")
    total = project.get_total_expenses()
    assert total == 30000
def test_expenses_by_category():
    clear_data()
    project.add_expense(15000, "Food", "Pizza", "2025-06-03")
    project.add_expense(5000, "Transport", "Coffee", "2025-06-04")
    assert project.get_expenses_by_category("Food") == 15000
    assert project.get_expenses_by_category("Transport") == 5000
def test_expenses_by_date_range():
    clear_data()
    project.add_expense(8000, "Entertainment", "Movie", "2025-11-15")
    project.add_expense(12000, "Food", "Burger", "2025-11-16")
    result = project.get_expenses_by_date_range("2025-11-15", "2025-11-16")
    assert len(result) == 2
    assert result[0]["description"] == "Movie"
def test_monthly_summary():
    clear_data()
    project.add_expense(10000, "Food", "Sushi", "2025-05-10")
    project.add_expense(20000, "Transport", "Train ticket", "2025-05-15")
    summary = project.get_monthly_expenses(2025, 5)
    assert summary["total"] == 30000
    assert summary["average_per_day"] == 15000
def test_top_categories():
    clear_data()
    project.add_expense(5000, "Food", "Salad", "2025-04-01")
    project.add_expense(15000, "Food", "Steak", "2025-04-02")
    top = project.get_top_categories()
    assert top[0][0] in ["Food"]
def test_search_by_description():
    clear_data()
    project.add_expense(7000, "Misc", "Book purchase", "2025-03-05")
    results = project.search_by_description("book")
    assert len(results) == 1
    assert results[0]["category"] == "Misc"
def test_sort_expenses_by_amount():
    clear_data()
    project.add_expense(3000, "Snacks", "Chips", "2025-02-10")
    project.add_expense(8000, "Groceries", "Vegetables", "2025-02-11")
    sorted_expenses = project.sort_expenses("amount")
    assert sorted_expenses[0]["amount"] == 8000

