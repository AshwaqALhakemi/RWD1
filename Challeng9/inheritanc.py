class Person(object):


    def __init__(self, name):
        self.name = name


    def getName(self):
        return self.name


    def isEmployee(self):
        return False



class Employee(Person):


    def isEmployee(self):
        return True



emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())


class Person(object):


    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)



class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post


        Person.__init__(self, name, idnumber)




a = Employee('Rahul', 886012, 200000, "Intern")


a.display()