import pandas as pd
import onnxruntime as ort
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from statics import predict_threat
import re


# LOAD DATA
# DATA_PATH ='models/BesafeV1_1.0.00.onnx'

# TESTING 
while True:
    user_input = input("Enter a sentence (or 'exit'): ")

    if user_input.lower() == "exit":
        break

    result = predict_threat(user_input)
    label, prob = result
    print(f"Text: {user_input}\nPreediction: {label} (probability: {prob:.4f})")