import numpy as np
import pandas as pd
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

# Step 1 : Load the Data

#-------------------------------------------------------------------------------
#   Function name : LoadData
#   Description :   Load data from csv
#   input :         Name of csv file  
#   output :        Data Frame
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded succefully")
    print(df.head())

    return df

# Step 2 : Data preprocessing

#-------------------------------------------------------------------------------
#   Function name : PreProcessData
#   Description :   Performs data analysis
#   input :         Data frame 
#   output :        Updated data frame
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def PreProcessData(df):
    df = df.drop([
        "Passengerid",
        "name"
    ],
    errors = "ignore"
    )

    # Handle missing values

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numerical
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype = int
    )
    
    print(df.head())

    print("Data preprocessing completed")

    return df

#-------------------------------------------------------------------------------
#   Function name : main
#   Description :   entry function
#   input :         none  
#   output :        none
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def main():
    #Step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step2
    df = PreProcessData(df)

if __name__ == "__main__":
    main()