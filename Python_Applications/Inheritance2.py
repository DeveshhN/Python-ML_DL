class Base:
    def __init__(self):
        print("Inside Base constructor")

class Derived(Base):
    def __init__(self):
        print("Inside Derived Constructor")
 
bobj = Base()
