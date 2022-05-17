import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

class LSTMClassifier:
    def __init__(self):
        self.model = pickle.load(open('models/lstm.pkl', 'rb'))
        self.tokenizer = pickle.load(open('models/lstm_tokenizer.pkl', 'rb'))

    def predict(self, sentence):
        testing_sequences = self.tokenizer.texts_to_sequences([sentence])

        testing_padded = np.array(pad_sequences(testing_sequences, maxlen=100, padding='post', truncating='post'))

        prediction = self.model.predict(testing_padded)

        return [(p > 0.8)[0] for p in prediction]
        
class BERTClassifier:
    def __init__(self):
        self.model = pickle.load(open('models/bert.pkl', 'rb'))
        self.tokenizer = pickle.load(open('models/bert_tokenizer.pkl', 'rb'))

    def encoder(self, sentences):
        ids = []
        for sentence in sentences:
          encoding = self.tokenizer.encode_plus(
          sentence,
          max_length=16,
          truncation = True,
          add_special_tokens=True,
          return_token_type_ids=False,
          pad_to_max_length=True,
          return_attention_mask=False)
          ids.append(encoding['input_ids'])
        return ids


    def predict(self, sentence):
        ids = tf.convert_to_tensor(self.encoder([sentence]))

        prediction = self.model.predict(ids)
        return [(p > 0.8)[0] for p in prediction]
