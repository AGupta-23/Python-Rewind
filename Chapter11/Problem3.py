# 3. Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
# ‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
# the value of increment based on the salary.

class Employee:

    def __init__(self, salary, increment):

        # Original salary
        self.salary = salary

        # Increment percentage
        self.increment = increment


    # Getter Property
    @property
    def salaryAfterIncrement(self):

        # Formula:
        # final salary = salary + increment %

        return self.salary + (self.salary * self.increment / 100)


    # Setter Property
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):

        # Updating increment according to new salary

        self.increment = ((new_salary / self.salary) - 1) * 100


# Object
e = Employee(50000, 20)

# Getter runs
print(e.salaryAfterIncrement)


# Setter runs
e.salaryAfterIncrement = 70000

print(e.increment)