import os
import time
import json
from application.salary import calculate_salaries
from application.db.people import get_employees


def load_employees_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def display_employee_data(employees):
    for employee in employees:
        print(f"Name: {employee['name']}, Position: {
              employee['position']}, Salary: {employee['salary']}")


def main():
    file_path = 'employees.json'
    last_modified_time = None

    while True:
        try:
            current_modified_time = os.path.getmtime(file_path)

            if last_modified_time is None or current_modified_time != last_modified_time:
                print("Файл обновлен, загружаем данные...")
                employees = load_employees_from_json(file_path)
                last_modified_time = current_modified_time

                display_employee_data(employees)

                calculate_salaries(employees)

            time.sleep(5)

        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            time.sleep(5)
        except json.JSONDecodeError:
            print("Ошибка при чтении JSON файла.")
            time.sleep(5)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            time.sleep(5)


if __name__ == '__main__':
    main()
