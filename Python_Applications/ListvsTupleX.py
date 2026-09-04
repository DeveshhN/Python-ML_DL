#--------------------------------------------------------
#              List   Tuple
#-------------------------------------------------------
#ORDERED        YES    YES
#INDEXED        YES    YES
#MUTABLE        YES     NO
#Heterogeneous  YES    YES
#-------------------------------------------------------

def main():
    Data1 = [10,3.14,True,"Pune"]  #List
    Data2 = (10,3.14,True,"Pune")  #Tuple

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[2])


if __name__ == "__main__":
    main()