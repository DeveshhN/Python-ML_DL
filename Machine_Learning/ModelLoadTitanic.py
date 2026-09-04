import pandas as pd
import joblib

def LoadModel(Filename):
    model = joblib.load(Filename)

    print("Model loaded successfully")

    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter Info")

    Pclass = int(input("Enter either (1/2/3)"))
    Sex =   int(input("Enter Sex : (Female- 0/Male-1)"))
    Age =   float(input("Enter Age : "))
    Sibsp = int(input("Enter sibsp : "))
    Parch = int(input("Enter Parch : "))
    Fare = int(input("Enter Fare : "))
    Embarked = float(input("Enter Embarked : (0/1/2) :  "))

    passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Sex" : Sex,
        "Age" : Age,
        "Sibsp" : Sibsp,
        "Parch" : Parch,
        "Fare" : Fare,
        "Embarked__1.0" : 1 is Embarked == 1 else 0,
        "Embarked__2.0" : 1 is Embarked == 2 else 0
    }])

    passenger = passenger[model.feature_names_in_]

    result = model.predict(passenger)
    return(result)

def main():
    model = LoadModel("MarvellousTitanic.pkl")
    PredictPassenger(model)

if __name__ == "__main__":
    main()