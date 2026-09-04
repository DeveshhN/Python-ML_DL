from sklearn.datasets import load_iris

def main():

    print("-"*51)
    print("Iris classification case study")
    print("-"*51)

    Dataset = load_iris()

    print(Dataset)

if __name__ == "__main__":
    main()