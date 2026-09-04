import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [27,28,25],
        "City" : ["Pune","Kolhapur","Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj)

    ##    Not Allowed      print(dobj[0])
    
    print(dobj["Age"])
    
if __name__ == "__main__":
    main()