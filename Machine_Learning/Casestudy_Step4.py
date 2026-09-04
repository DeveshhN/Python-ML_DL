import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*72

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

#####################################################
# Step 3 : Decide Independent or Dependent variables
#####################################################

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

################################################
# Step 4 : Visualisation of Dataset
################################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

#Scatter plot 
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label=sp)

plt.title("Marvellous Iris Case study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()