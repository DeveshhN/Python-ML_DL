import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-"*81

    #Step 1 : Load the Data from CSV File

    print(border)
    print("Step1 : Load the data from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset : ")
    print(df.head())
    print(border)

    #Step 2 : Clean the DataSet

    print(border)
    print("Step 2 : Clean the DataSet")
    print(border)

    df.dropna(inplace=True)

    print("Shape of dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(border)

    #Step # : Separate Independent and Dependent Variables

    print(border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print("Input Colums : ",X.columns.tolist())
    print("Output Columns : Class")
    print(border)

    #Step 4 : Split the dataset for training and testing

    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of training and testing data ")

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    print(border)

    #Step 5 : Feature Scaling

    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature Scaling Completed")

    print(border)

    #Step 6 : Buil the Model

    print(border)
    print("Step 6 : Build the Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)

    print("Classification model is created")

    #Step 7 : Train the model
    
    model = model.fit(X_train_scaled,Y_train)

    print(border)
    print("Step 7 : Train the model")
    print(border)

    print("Model Training Completed")
    print(border)

    #Step 7 : Test the model
        
    print(border)
    print("Step 8 : Test the model")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy*100)
    print(border)


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()