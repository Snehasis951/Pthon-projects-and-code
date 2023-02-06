class employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + lname + "@gmail.com"
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
if __name__ == "__main__":
    Snehasis = employee("Snehasis", "Mondal", 55000)
    Suranjana = employee("Suranjana", "Mondal", 55000)
    print(Snehasis.email, Suranjana.email)
# lovish = employee.from_str("lovish-jackson-70000")

print(employee.isopen("Tues day"))


# print(lovish.salary)

a = 5
print(a.__add__(6))
