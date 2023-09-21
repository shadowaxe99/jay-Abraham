
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load data
with open('../data/jay_abraham_teachings.txt', 'r') as file:
    data = file.read().replace('\n', '')

# Tokenize data
tokens = word_tokenize(data)
vocab_size = len(set(tokens))

# Prepare data for training
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(tokens)
sequences = tokenizer.texts_to_sequences(tokens)

# Prepare inputs and targets
inputs, targets = sequences[:-1], sequences[1:]
max_sequence_len = max([len(x) for x in inputs])
inputs = pad_sequences(inputs, maxlen=max_sequence_len, padding='pre')
targets = tf.keras.utils.to_categorical(targets, num_classes=vocab_size)

# Define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=max_sequence_len))
model.add(LSTM(150, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(vocab_size, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(inputs, targets, epochs=100, verbose=2)

# Save model
model.save('../models/nlp_model.h5')
