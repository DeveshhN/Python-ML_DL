import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(DataPath):
    # Step 1 : Load the Data

    Border = "-"*72

    print(Border)
    print("Step 1 : Load the Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())

    # Step 2 : Remove unwanted columns

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns= ["Unnamed: 0"])

    print(df.head())

    # Step 3 : Check missing values

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Total missing values : ")
    print(df.isnull().sum())
    print(Border)

    # Step 4 : Statistical Summary

    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border)

    print(df.describe())

    # Step 5 : Corelation

    print(Border)
    print("Step 5 : Corelation")
    print(Border)

    print(df.corr())

    # Step 6 : Separate independent and dependent variables

    print(Border)
    print("Step 6 : Separate Independent and Dependent variables")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables : ")
    print(X.head())

    print("Dependent variables : ")
    print(Y.head())

def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()