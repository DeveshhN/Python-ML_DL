from sklearn.datasets import load_iris

def main():

    print("-"*51)
    print("Iris classification case study")
    print("-"*51)

    Dataset = load_iris()

    #Meta Data of the dataset
    print("Independent variables are:")
    print(Dataset.feature_names)

    print("Dependent variables are : ")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()