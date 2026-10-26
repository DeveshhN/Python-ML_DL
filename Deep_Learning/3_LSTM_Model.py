# Step 1 : Import required libraries

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding , LSTM , Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

#######################################################################
# Step 2 : Configuration of values
#######################################################################

VOCAB_SIZE = 10000 # consider most frequent 10000 unique words
MAX_LENGTH = 200   # consider maximum 200 words in review

#######################################################################
# Step 3 : Load the IMDB dataset
#######################################################################

print("-"*72)
print("Movie Review Sentiment Analysis using LSTM")
print("-"*72)

print("Loading the Dataset.....")

(X_train , Y_train) , (X_test, Y_test) = imdb.load_data(num_words = VOCAB_SIZE)

print("IMDB Dataset loaded successfully")

print("Number of training reviews : ",len(X_train))
print("Number of testing  reviews : ",len(X_test))

#######################################################################
# X_train :  Reviews used for training 
# Y_train :  Actual sentiments of training 
# X_test  :  Reviews used for testing
# Y_test  :  Actual sentiments of testing

# Sentiments : 
# 0 -> Negative Sentiment
# 1 -> Positive Sentiment
#######################################################################

#######################################################################
# Step 4 : Load the word dictionary 
#######################################################################

word_index = imdb.get_word_index()

# Dictionary contains mapping of word and its corresponding number
# Eg : Drishyam is good movie           -> (20 56 78 43)
# 20 -> Drishyam
# 56 -> is 
# 78 -> good 
# 43 -> movie

#######################################################################
# Step 5 : Create reverse dictionary
#######################################################################

reverse_word_index = {}

for word , index in word_index.items():
    reverse_word_index[index+3] = word

#######################################################################
# Step 6 : Function to decode the review (number to word)
#######################################################################

def DecodeReview(encoded_review) : 
    words = []

    for number in encoded_review:
        if number >= 3: # ignore first 3
            word = reverse_word_index.get(number,"?")
            words.append(word)

    return " ".join(words) # Join the list of words

#######################################################################
# Step 7 : Display sample reviews
#######################################################################

print("-"*72)
print("------------------------Sample Reviews--------------------------")
print("-"*72)

for i in range(3,7):
    review = DecodeReview(X_train[i])

    print("-"*72)
    print("Review number : ",i+1)
    print("Review : ")
    print(review)
    print("-"*72)

    if Y_train[i] == 1:
        print("Sentiment : Positive")
    else:
        print("Sentiment : Negative")

#######################################################################
# Step 8 : Padding
#######################################################################

X_train_padded = pad_sequences(
    X_train,
    maxlen = MAX_LENGTH
)

X_test_padded = pad_sequences(
    X_test,
    maxlen = MAX_LENGTH
)

print("Training data shape : ",X_train_padded.shape)
print("Testing data shape : ",X_test_padded.shape)

#######################################################################
# Step 9 : Create LSTM Model
#######################################################################

model = Sequential()

model.add(
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim= 32        # Each word is represented in 32 values
    )
)

model.add(
    LSTM(
        units = 64            # Size of LSTM hidden state
    )
)

model.add(
    Dense(
        units = 1,            # one output
        activation="sigmoid"  # Used to produce probability
    )
)

# Project architecture
# Review -> Embedding -> LSTM -> Dense -> Sigmoid -> Positive/Negative

#######################################################################
# Step 10 : Compile the model
#######################################################################

model.compile(
    optimizer = "adam",           # Algorithm to update weights
    loss = "binary_crossentropy", # Loss function
    metrics = ["accuracy"]        # Measure classification accuracy
)

print("Model compiled successfully")

#######################################################################
# Step 11 : Train the model
#######################################################################

print("Model Training")

model.fit(
    X_train_padded,           # input training reviews
    Y_train,                  # Actual sentiment labels
    epochs = 5,           
    batch_size = 64,          # Process 64 reviews in 1 batch
    validation_split = 0.2    # Use 20% training for validation         
)

print("Model training completed")

#######################################################################
# Step 12 : Evaluate the model
#######################################################################

accuracy = model.evaluate(
    X_train_padded,           # Testing reviews
    Y_test,                   # Actual testing labels
    verbose = 0
)

print("Testing accuracy : ",accuracy)

#######################################################################
# Step 13 : Predict the review
#######################################################################

original_review = X_test[0]
decoded_review = DecodeReview(original_review)

print("Review given to the model")
print(decoded_review)

#######################################################################
# Step 14 : Get the actual sentiment 
#######################################################################

