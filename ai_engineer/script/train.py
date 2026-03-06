import pandas as pd
import tensorflow as tf
from keras import models
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Embedding,LSTM,Dense,Dropout,Bidirectional
from tensorflow.keras.optimizers import Adam
from src.test import clean_text
import re

# MODEL FUNCTION
def my_model (vocab_size, embedding_dim,input_len):
    model = models.Sequential([
    Embedding(vocab_size, embedding_dim, input_length=input_len),
    Bidirectional(LSTM(LSTM_UNITS, dropout=0.3, return_sequences=False)),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
    ])

    model.compile(
    optimizer=Adam(learning_rate=0.00001),
    loss='binary_crossentropy',
    metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
    )
    model.build(input_shape=(None, MAX_LEN))
    return model

# LOAD DATA
DATA_PATH ='testing/finalLargeDs.csv'
TOKENIZER_PATH= 'testing/tokenizer'
MODEL_PATH = 'testing/test.h5'
data =pd.read_csv(DATA_PATH)

# CONSTANT VARIABLES
VOCAB_SIZE =10000
MAX_LEN=100
EMBEDDING_DIM =128
LSTM_UNITS =32
EPOCHS =10

# CLEAN DATA
data['cleaned_text'] =data['Text'].apply(clean_text)

# FEATURE AND LABEL ASSIGNMENT
x=data['cleaned_text'].values
y=data['Label'].values.astype(int)

# SPLITTING
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, shuffle=True, random_state=42,stratify=y)

# DATA EXPLORATION
# unique_labels, counts = np.unique(y_test, return_counts=True)


# TOKENIZER INSTANTIATION
tokenizer=Tokenizer(num_words=VOCAB_SIZE,oov_token='<OOV>')
tokenizer.fit_on_texts(x_train)

# Sequnces
train_sequence = tokenizer.texts_to_sequences(x_train)
test_sequence=tokenizer.texts_to_sequences(x_test)

# Padding and truncation
train_padded=pad_sequences(train_sequence,maxlen= MAX_LEN,padding='post',truncating='post')
test_padded=pad_sequences(test_sequence,maxlen= MAX_LEN,padding='post',truncating='post')

# CALLBACKS
callbacks=[
    tf.keras.callbacks.EarlyStopping(patience=5,restore_best_weights=True),#for early stopping on unchanged metrics
    tf.keras.callbacks.ModelCheckpoint(filepath=MODEL_PATH,save_best_only=True) # for model checking per epoch and auto saving
]

# TRAINING
model = my_model(VOCAB_SIZE,EMBEDDING_DIM,MAX_LEN)
history =model.fit(train_padded,y_train,epochs=EPOCHS,shuffle=True,validation_split=0.3,callbacks=callbacks,batch_size=32)

# STORE TOKENIZER
# with open(TOKENIZER_PATH, 'wb') as f:
#     pickle.dump(tokenizer, f)