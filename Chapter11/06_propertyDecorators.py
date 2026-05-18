class Employee:
    a=1

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
e.name="ABHIDHA GUPTA"   #calls the setter method automatically
print(e.fname)
print(e.lname)


# Main Concept

# Property decorators allow methods to behave like variables.

# Without property decorators, you would normally write:

# e.set_name("ABHIDHA GUPTA")
# print(e.get_name())

# But with property decorators:

# e.name = "ABHIDHA GUPTA"
# print(e.name)