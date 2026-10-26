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