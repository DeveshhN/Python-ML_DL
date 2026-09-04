no = 11                                          #GLOBAL Variable

def Display():
    a = 21                                       #LOCAL Variable
    print("From Display : ", no)
    print("From Display value of a is : ",a)     

def Demo():
    print("From Demo value of a is: ",a)
    print("From Demo : ", no)    

Display()
Demo()