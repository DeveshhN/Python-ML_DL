sentence = "food was not good"
#Timestep    1    2   3   4
#Token       1    2   5   3

words = sentence.split()

print("Actual Sentence is : ",sentence)

for index , word in enumerate(words):
    print("Time Step : ",index+1, " : ",word)