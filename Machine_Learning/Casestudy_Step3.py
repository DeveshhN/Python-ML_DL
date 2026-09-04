import pandas as pd

Border = "-"*51

################################################
# Step 1 : Load the Data Set
################################################

Border = "-"*51
print(Border)
print("Step 1  : Load the Data Set")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Data set loaded sucessfully")
print("Initial entries from dataset are :")
print(df.head())

################################################
# Step 2 : Data Analysis (EDA)
################################################


print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum())

print("Class distribution (species column) : ")
print(df["species"].value_counts())

print("Statistical report of datasets : ")
print(df.describe())

################################################
# Step 3 : Decide Independent or Dependent variables
################################################

print(Border)
print("Step 3 : Decide Independent or Dependent variables")
print(Border)

#X = Independent Variable / Features
#Y = Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ", X.shape)
print("Y Shape : ",Y.shape)