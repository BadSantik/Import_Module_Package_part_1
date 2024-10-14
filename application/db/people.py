from datetime import datetime
import json


def get_employees():
    print(f"Getting employees on {
          datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    with open('employees.json', 'r', encoding='utf-8') as file:
        employees = json.load(file)
    return employees
