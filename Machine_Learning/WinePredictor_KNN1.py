import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-"*81

    print(border)
    print("Step1 : Load the data from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset : ")
    print(df.head())
    print(border)

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()