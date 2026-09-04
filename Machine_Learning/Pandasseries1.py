import pandas as pd

def main():
    Data = [11,21,31,51]

    print(Data)

    sobj = pd.Series(Data)

    print(sobj)

if __name__ == "__main__":
    main()