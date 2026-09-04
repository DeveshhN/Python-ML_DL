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

