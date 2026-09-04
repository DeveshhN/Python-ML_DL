class Demo:
    def __init__(self):
        print("Inside consructor")

    def __del__(self):
        print("Inside Destructor")
    
obj1 = Demo()
obj2 = Demo()

print("End of Application")
