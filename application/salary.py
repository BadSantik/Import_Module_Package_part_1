def calculate_salaries(employees):
    print("Calculating salaries...")
    for employee in employees:
        salary = employee['salary']
        print(f"Name: {employee['name']}, Position: {
              employee['position']}, Calculated Salary: {salary}")
