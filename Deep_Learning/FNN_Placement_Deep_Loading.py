#-------------------------------------------------
# Deep learning pipeline
#-------------------------------------------------
#1. Read the data from csv 
#2. Data analysis
#3. Preprocessing
#4. Train, test, split
#5. Feature scaling
#6. FNN model training
#7. Model evaluation
#8. Graphical Representation
#9. Model preserve
#10. Model loading and preserve
#11. Test unseen data
#-------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#-------------------------------------------------
#1. Read the data from csv 
#-------------------------------------------------

print("Step 1 : Read the data from csv")

data = pd.read_csv("placement_data.csv")
print(data)

#-------------------------------------------------
#2. Data Analysis
#-------------------------------------------------

print("Step 2 : Data Analysis")

print("First five rows : ")
print(data.head())

print("Column names : ")
print(data.columns)

print("Shape of dataset : ")
print(data.shape)

print("Statistical summarry : ")
print(data.describe())

#-------------------------------------------------
#3. Preprocessing
#-------------------------------------------------

print("Step 3 : Preprocessing")

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input features : ")
print(X.head())

print("Target : ")
print(Y.head())

#-------------------------------------------------
#4. Train, test, split
#-------------------------------------------------

print("Step 4 : Train, test, split")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30 , random_state=42)

print("Training input shape : ",X_train.shape)
print("Testing input shape : ",X_test.shape)
print("Training output shape : ",Y_train.shape)
print("Testing output shape : ",Y_test.shape)

#-------------------------------------------------
#5. Feature scaling
#-------------------------------------------------

print("Step 5 : Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train) 
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled training data : ")
print(X_train_scaled[:5])

#-------------------------------------------------
#6. FNN model training
#-------------------------------------------------

print("Step 6 : FNN model creation and training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Model training begins")

model.fit(X_train_scaled,Y_train)

print("Model training completed")

#-------------------------------------------------
#7. Model evaluation
#-------------------------------------------------

print("Step 7 : Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test , Y_pred)

print("Accuracy is : ",accuracy)

cm = confusion_matrix(Y_test , Y_pred)

print("Confusion matrix : ",cm)

print("Predict the probability : ")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#-------------------------------------------------
#8. Graphical Representation
#-------------------------------------------------

print("Step 8 : Graphical Representation")

#-------------------------------------------------
#9. Model preserve
#-------------------------------------------------

#print("Step 9 : Model preserve")

#joblib.dump(model,"placement_fnn_model.pkl")
#joblib.dump(scalar,"placement_scalar.pkl")

#print("Model and scalar gets dump successfully")

#-------------------------------------------------
#10. Model loading and preserve
#-------------------------------------------------

print("Step 10 : Model loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("Model gets loaded successfully")

#-------------------------------------------------
#11. Test unseen data
# Aptitude :       70
# Coding :         75
# Communication :  80
# Academics :      85
# Intership :      1
#-------------------------------------------------

print("Step 11 : Test unseen data")

new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probability = loaded_model.predict_proba(new_student_scaled)

print("New student's data : ")
print(new_student)

print("Prediction  probability : ",new_probability)

if new_prediction[0] == 1:
    print("Predictions : Placed")
else:
    print("Prediction : Not Placed")

