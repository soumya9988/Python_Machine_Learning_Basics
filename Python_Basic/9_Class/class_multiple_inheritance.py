class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def return_person(self):
        return 'Employee: ' + self.name + ', SSN: ' + self.ssn


class Employee:
    def __init__(self, e_id, salary):
        self.e_id = e_id
        self.salary = salary

    def return_emp_det(self):
        return 'Employee id:' + self.e_id


class Chairman(Person, Employee):
    def __init__(self, name, ssn, e_id, salary, no_of_employees):
        Person.__init__(self, name,ssn)
        Employee.__init__(self,e_id, salary)
        self.n_o_e = no_of_employees

    def print_details(self):
        return self.return_person(), self.return_emp_det(), self.n_o_e


c1 = Chairman('Mickey Mouse', 'E123FT', 'C123', 125000, 3000)
print(c1.print_details())
print(issubclass(Chairman, Employee))
print(issubclass(Chairman, Person))
print(issubclass(Person, Employee))
print(isinstance(c1, Employee))

