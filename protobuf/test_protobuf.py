import employees_pb2 as emp

# Add employee 1
ram = emp.Employee()
ram.id = 1001
ram.name = 'Ram'
ram.salary = 5000

# add employee2
shyam = emp.Employee()
shyam.id = 1002
shyam.name = 'Shyam'
shyam.salary = 10000

# construct employees
employees = emp.Employees()
employees.employees.append(ram)
employees.employees.append(shyam)

print(employees)
bytes = employees.SerializeToString()
print(f'Serailzied string is {bytes}')

# Create new objecgt and feed data
new_employees = emp.Employees()
new_employees.ParseFromString(bytes)
print(f' Parsed from string: {new_employees}')

