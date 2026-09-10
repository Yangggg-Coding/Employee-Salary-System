employees = {}

def AddNewEmployee():
    print("\n--- Adding New Employee ---")
    emp_id = int(input("ID : "))
    if emp_id in employees:
        print("ID already exists.")
        return
    
    name = input("Name: ")
    email = input("Email: ")
    duration = int(input("Duration (Years): "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    bonus = int(input("Bonus: "))
    
    employees[emp_id] = {
        "name": name,
        "email": email,
        "duration": duration,
        "department": department,
        "salary": salary,
        "bonus": bonus,
    }
    print("Employee added.")

def ListAllEmployees():
    if not employees:
        print("No employees.")
        return
    print("===============================================")
    for eid in employees:        
        emp = employees[eid]
        print(f"\nID: {eid}")
        print("Name      :", emp["name"])
        print("Email     :", emp["email"])
        print("Duration  :", emp["duration"],"years")
        print("Department:", emp["department"])
        print("Salary    :$", emp["salary"])
        print("Bonus     :$", emp["bonus"])

def UpdateInfoById():
    emp_id = int(input("Enter ID : "))
    emp = employees.get(emp_id)
    if not emp:
        print("Invalid ID")
        return
    
    print("1. Duration\n2. Salary\n3. Bonus ")
    choice = int(input("Choice: "))
    if choice == 1:
        emp["duration"] = int(input("New Duration (years): "))
    elif choice == 2:
        emp["salary"] = int(input("New Salary: "))
    else:
        emp["bonus"] = int(input("New Bonus: "))
        
    print("\nInfo has been updated.")

def DeleteInformation():
    emp_id = int(input("Enter ID to delete: "))
    if emp_id in employees:
        del employees[emp_id]
        print("\nEmployee deleted.")
    else:
        print("Invalid ID")

def SearchInfo():
    emp_id = int(input("Enter ID to search: "))
    emp = employees.get(emp_id)
    if emp:
        print("Name      :", emp["name"])
        print("Email     :", emp["email"])
        print("Duration  :", emp["duration"], "years")
        print("Department:", emp["department"])
        print("Salary    :$", emp["salary"])
        print("Bonus     :$", emp["bonus"])
    else:
        print("Invalid ID")


while True:
    try:
        print("===============================================")
        print("                     MENU                     ")
        print("===============================================\n")
        print(" 1. Add New Employee")
        print(" 2. Display All Employee Information")
        print(" 3. Update Employee Information")
        print(" 4. Delete Employee Information")
        print(" 5. Search Employee Information")
        print(" 6. Exit The Program")
        choice = int(input("Choice: "))
        if choice == 1:AddNewEmployee()
        elif choice == 2:ListAllEmployees()
        elif choice == 3:UpdateInfoById()
        elif choice == 4:DeleteInformation()
        elif choice == 5:SearchInfo()
        elif choice == 6:
            print("\nGood Bye User!\n")
            break
        else:
            print("Please enter number between 1-6.")
    except ValueError:
        print("Please enter only number!")
