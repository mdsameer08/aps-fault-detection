from dataclasses import dataclass
@dataclass
class Employee:
    emp_name:str
    age:int
emp=Employee(emp_name="sameer", age=23)
#emp.emp_name
print(emp.emp_name)