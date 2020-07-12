class Employee():
    
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    def give_raise(self,add_salary=5000):
        self.salary += add_salary

