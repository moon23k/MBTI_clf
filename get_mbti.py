import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string
from joblib import load
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
import pickle


def clean_text(text):
    text = ' '.join(text)
    #words = str(text).split()
    words = text.split()
    words = [i.lower() + " " for i in words]
    words = [i for i in words if not "http" in i]
    words = " ".join(words)
    words = words.translate(words.maketrans('', '', string.punctuation))
    
    return words



def get_result(words):
    model_path = os.getcwd() + '/checkpoints/mbti_clf3.pickle'
    vect_path = os.getcwd() + '/checkpoints/vectorizer2.pickle'
    le_path = os.getcwd() + '/checkpoints/label_encoder2.pickle'

    vect = pickle.load(open(vect_path, 'rb'))
    target_encoder = pickle.load(open(le_path, 'rb'))
    #model = pickle.load(open(model_path, 'rb'))
    model = XGBClassifier()
    model.load_model(model_path)

    '''
    vect = load(vect_path)
    model = load(model_path)
    target_encoder = load(le_path)
    '''

    data = vect.transform([words]).toarray()
    result = model.predict(data)
    result = target_encoder.inverse_transform(result)

    return result

