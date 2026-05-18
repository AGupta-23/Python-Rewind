class Numbers:

    def __init__(self,x):
        self.x=x

    def __add__(self,num):
        return self.x+num.x

n=Numbers(1)
m=Numbers(2)
print(n+m)   #print(n.__add__(m))
# You created your own object and taught Python how + should work for it.
