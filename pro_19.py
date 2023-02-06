class employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod 
    def change_increment(cls, amount):
        cls.increment = amount
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == "Sunday":
            return False
        else:
            return True

class programmer(employee):
    def __init__(self, fname, lname, salary, prolang, exp):
        super().__init__(fname, lname, salary)
        self.prolang = prolang
        self.exp = exp
Snehasis = employee("Snehasis", "Mondal", 55000, "Python", "4 yrs")
print(Snehasis.exp)
Suranjana = employee("Suranjana", "Mondal", 55000)
lovish = employee.from_str("lovish-jackson-70000")

print(employee.isopen("Tues day"))
# Snehasis.fname = "Snehasis"
# Snehasis.lname = "Mondal"
# Snehasis.salary = "55000"
# 
# Suranjana.fname = "Suranjana"
# Suranjana.lname = "Mondal"
# Suranjana.salary = "55000"

# print(Snehasis.salary)
# Snehasis.increase()
# print(Snehasis.salary)

# print(Suranjana.fname, Snehasis.fname)
# print(Snehasis.salary)
# employee.change_increment(2)
# Snehasis.increase()
# print(Snehasis.salary)

print(lovish.salary)
