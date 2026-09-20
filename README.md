# Employee Salary System

Console-based CRUD application for managing employee records, built in Python using a dictionary as the data store.

## Features

- Add a new employee (ID, name, email, years of service, department, salary, bonus)
- List all employees
- Update an employee's duration, salary, or bonus
- Delete an employee by ID
- Search for an employee by ID
- Input validation on numeric fields, with error handling for non-numeric input

## How to run

Requires Python 3, no external libraries.

```
python3 employee_salary_system.py
```

## Menu

```
1. Add New Employee
2. Display All Employee Information
3. Update Employee Information
4. Delete Employee Information
5. Search Employee Information
6. Exit The Program
```

## Data storage

Records are held in memory in a Python dictionary while the program runs. Data does not persist between runs, restarting the program clears all records. No database or file storage is used.

## Why I built this

Practice project for core Python: dictionaries, functions, loops, and input validation, not a production system.
