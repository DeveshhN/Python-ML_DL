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

#-------------------------------------------------------------------------------
#   Function name : main
#   Description :   entry function
#   input :         none  
#   output :        none
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()