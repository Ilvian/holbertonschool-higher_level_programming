#!/usr/bin/python3
database = {
        "Mentors": ["Evis", "Andi"],
        "Software Engineers": ["Romeo", "Ergi", "Ilvian", "Izabela", "Silvia", "Ersida", "Arlind"],
        "Sponsors": ["Lajthiza", "Ama Caffe", "Ping Pong Table (R.I.P)"]
        }

def add_employee():
    department = input("Enter department name: ")
    name = input("Enter employee name: ")

    if department in database:
        database[department].append(name)
    else:
        database[department] = [name]
    print(f"{name} added to {department}.")

def remove_employee():
    department = input("Enter department name: ")
    name = input("Enter employee name: ")

    if department in database and name in database[department]:
        database[department].remove(name)
        print(f"{name} removed from {department}.")
    else:
        print("Department or employee does not exist.")

def view_department_employees():
    department = input("Enter department name: ")
    if department in database:
        print(f"Employees in {department}: {', '.join(database[department])}")
    else:
        print("Department not found.")

def list_all_departments():
    for department, name in database.items():
        print(f"{department}: {', '.join(name)}")

def department_with_most_employees():
    if not database:
        print("The database is empty.")
        return
    max_emp = 0
    max_dep = ""
    for department, employees in database.items():
        if len(employees) > max_emp:
            max_emp = len(employees)
            max_dep = department
    print(f"The department with most employees is: {max_dep} with {max_emp} employees.")

def move_employee():
    name = input("Enter employee name: ")
    curr_dep = input("Current department: ")
    new_dep = input("Destination department: ")
    if curr_dep in database and new_dep in database and name in database[curr_dep]:
        database[curr_dep].remove(name)
        database[new_dep].append(name)
        print(f"{name} moved from {curr_dep} to {new_dep}.")
    else:
        print("Departments or employee doesnt exist.")

def total_employees():
    tot_emp = sum(len(name) for name in database.values())
    print(f"Total employee number: {tot_emp}")

def find_employee_by_name():
    name = input("Enter name of employee: ")
    found = False
    for department, employee in database.items():
        if name in employee:
            print(f"{name} is in {department}.")
            found = True
    if not found:
        print(f"{name} not found in any department.")

def main():
    while True:
        print()
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Department Employees")
        print("4. List All Departments")
        print("5. Department with Most Employees")
        print("6. Move Employee")
        print("7. Total Employees")
        print("8. Find Employee by Name")
        print("9. Exit")
        choice = input("Choose your action: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            view_department_employees()
        elif choice == '4':
            list_all_departments()
        elif choice == '5':
            department_with_most_employees()
        elif choice == '6':
            move_employee()
        elif choice == '7':
            total_employees()
        elif choice == '8':
            find_employee_by_name()
        elif choice == '9':
            break
        else:
            print("Invalid choice!")
main()
