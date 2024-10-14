import matplotlib.pyplot as plt
import json


def load_employees_from_json(file_path):    
    with open(file_path, 'r', encoding='utf-8') as file:
        employees = json.load(file)
    return employees


def plot_salary_comparison(employees):    
    names = [employee['name'] for employee in employees]
    salaries = [employee['salary'] for employee in employees]

    plt.figure(figsize=(12, 10))
    plt.barh(names, salaries, color='skyblue')
    plt.title('Сравнение зарплат сотрудников')
    plt.xlabel('Зарплата')
    plt.ylabel('Сотрудники')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Показываем диаграмму
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    employees = load_employees_from_json('employees.json')
    plot_salary_comparison(employees)
