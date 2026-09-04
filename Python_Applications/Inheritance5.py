class Base:
    def fun(self):
        print("Inside Base fun")

class Derived(Base):
    def sun(self):
        print("Insider Derived sun")

dobj = Derived()

dobj.fun()
dobj.sun()