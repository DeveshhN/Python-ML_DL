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

# Step 3 : Spliting Data

#-------------------------------------------------------------------------------
#   Function name : SplitData
#   Description :   Performs splitting activity
#   input :         Data frame 
#   output :        4 subsets for training and testing
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state=42
    )

    print("Dataset spliting sucessfully completed")
    return X_train,X_test,Y_train,Y_test

# Step 4 : Training model

#-------------------------------------------------------------------------------
#   Function name : TrainModel
#   Description :   Performs model training
#   input :         Training features and labels
#   output :        Trained model
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def TrainModel(X_train,Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train,Y_train)

    print("Model trained successfully")

    return  model

# Step 5 : Evaluate model

#-------------------------------------------------------------------------------
#   Function name : EvaluateModel
#   Description :   Performs model evaluation
#   input :         Model ,testing data(features,labels)
#   output :        Null
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def EvaluateModel(model,X_test,Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy)

    print(confusion_matrix(Y_test,Y_pred))

# Step 6 : Preserve model

#-------------------------------------------------------------------------------
#   Function name : PreserveModel
#   Description :   Performs model preservation in .pkl file
#   input :         model
#   output :        None
#   Author :        Devesh S Narkhede
#   Data :          16/08/2003  
#-------------------------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved with name : ",filename)

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

    # Step3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    #Step4
    model = TrainModel(X_train,Y_train)

    #Step5
    EvaluateModel(model,X_test,Y_test)

    #Step6
    PreserveModel(model,"MarvellousTitanic.pkl")

if __name__ == "__main__":
    main()