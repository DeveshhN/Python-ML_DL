import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,SimpleRNN,Dense

# Step 1 : Load the Data
train_sentences = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terrible",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terrible"
]

train_labels = [
    1,0,1,0,1,0,1,0,1,0,1,0 
]

# Step 2 : Tokenisation

tokenizer = Tokenizer(oov_token = "<OOV>")

tokenizer.fit_on_texts(train_sentences)

# Step 3 : Convert Training Data into sequence

train_sequences = tokenizer.texts_to_sequences(train_sentences)

print("Training Sequences : ")

for sentence , sequence in zip(train_sentences,train_sequences):
    print(sentence, "->",sequence)
    print(" ")