import numpy as np
import math

#-----------------------------------------
# Step 1 : Input layer
#-----------------------------------------

x1 = 2.0
x2 = 3.0

print("Step 1 : Input layer")
print("Features : X")
print(f"x1 = {x1}")
print(f"x2 = {x2}")

#-----------------------------------------
# Step 2 : Hidden layer
#-----------------------------------------

print("Step 2 : Hidden layer (2 Neurons)")

print("Hidden Neuron 1 ")

w11 = 0.5
w12 = -0.2
b1 = 0.1

print("Weights : ")
print(f"w11                      : {w11}")
print(f"w12                      : {w12}")

print("Bias                     : ")
print(f"b                        : {b1}")

print("Weightesd sum            : z1 = (x1*w11 + x2*w12 + b1)")

z1 = ( x1 * w11) + (x2 * w12 ) + b1

print("Weighted sum             : ",z1)

h1 = max(0,z1)
print("Output of hidden Neuron 1 : ",h1)

#########################################################

print("Hidden Neuron 1")

w21 = 0.8
w22 = 0.4
b2 = -0.1

print("Weights : ")
print(f"w21                      : {w21}")
print(f"w22                      : {w22}")

print("Bias                     : ")
print(f"b                        : {b2}")

print("Weightesd sum            : z2 = (x1*w21 + x2*w22 + b2)")

z2 = ( x1 * w21) + (x2 * w22 ) + b2

print("Weighted sum             : ",z2)

h2 = max(0,z2)
print("Output of hidden Neuron 2 : ",h2)

#-----------------------------------------
# Step 3 : Output layer
#-----------------------------------------

w_out1 = 1.0
w_out2 = -1.5
b_out = 0.2

print("Step 3 : Output layer")

print("Weights : ")
print(f"w_out1 : {w_out1}")
print(f"w_out2 : {w_out2}")

print(f"Bias : {b_out}")

z_out = (h1*w_out1) + (h2*w_out2) + b_out

print("Weighted sum : ",z_out)

z = 1 / (1 + math.exp(-z_out))

print("-------------------------------------------------")
print("---Neural Network Summary---")
print("-------------------------------------------------")

print("Input Layer")
print(f"x1 : {x1}")
print(f"x2 : {x2}")

print("Hidden Layer")
print(f"h1 : {h1}")
print(f"h2 : {h2}")

print("Output layer")
print(f"z : {z}")

print("Prediction of Neural network")

if(z >= 0.5):
    print("Predicted as POSITIVE CLASS")
else:
    print("Predicted as NEGATIVE CLASS")