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
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0 
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

# Step 4 : Apply Padding

max_length = 4

X_train = pad_sequences(
    train_sequences,
    maxlen = max_length,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded training data : ")
print(X_train)

print("Training Labels : ")
print(Y_train)

# Step 5 : Calculate vocabulary size

vocab_size = len(tokenizer.word_index) + 1

print("Vocabulary size : ",vocab_size)

# Step 6 : Build RNN Model

model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=8,
        input_length=max_length
    )
)

model.add(
    SimpleRNN(
        units = 8,
        activation = "tanh"
    )
)

model.add(
    Dense(
        units = 1,
        activation = "sigmoid"
    )
)

# Step 7 : Compile the model

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

# Step 8 : Display Model 

model.build(input_shape = (None , max_length))

print("Model Architecture : ")
model.summary()

# Step 9 : Train the model

history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)

print("Model training completed !!")

# Step 10 : Create unseen data

test_sentences = [
    "service was amazing",
    "service was horrible",
    "experience was excellent",
    "experience was terrible"
]

# Step 11 : Convert text to sequence

test_sequences = tokenizer.texts_to_sequences(test_sentences)

X_test = pad_sequences(
    test_sequences,
    maxlen = max_length,
    padding = "pre"
)

# Step 12 : Predict the enstiment

for text , sequence , padded in zip (test_sentences,test_sequences,X_test):
    input_data = np.array([padded])

    prediction = model.predict(input_data , verbose = 0)

    probability = float(prediction[0][0])

    print("Sentece : ",text)
    print("Seq : ",sequence)
    print("Padded seq : ",padded)
    print("Prediction : ",probability)

    if probability <= 0.5:
        print("Prabability : Positive")
    else:
        print("Probability : Negative")