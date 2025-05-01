from ast import While
employee_data =  {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}


def add_employee():
  emp_id = int(input("Generate employee id: "))
  if emp_id in employee_data.keys():  
    print("Employee id already exists")
  else:
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = int(input("Enter employee salary: "))
    employee_data[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print("Employee added successfully")


def update_employee():
  emp_id = int(input("Enter employee id: "))
  if emp_id in employee_data.keys():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = int(input("Enter employee salary: "))
    employee_data[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print("Employee updated successfully")
  else:
    print("Employee id does not exist")

def view_employee():
  print(f"Employee data: {employee_data}")

def search_employee():
  emp_id = int(input("Enter employee id: "))
  if emp_id in employee_data.keys():
    print(f"Employee data: {employee_data[emp_id]}")


def delete_employee():
  emp_id = int(input("Enter employee id: "))
  if emp_id in employee_data.keys():
    del employee_data[emp_id]
    print("Employee deleted successfully")


action =''
while action != 'exit':
  action = input("Enter action on employee data (add/update/view/search/delete/exit): ").lower()
  if action == 'add':
    add_employee()
  elif action == 'update':
    update_employee()
  elif action == 'view':
    view_employee()
  elif action == 'search':
    search_employee()
  elif action == 'delete':
    delete_employee()
  elif action == 'exit':
    print("Exiting program")
  else:
    print("Invalid action")
