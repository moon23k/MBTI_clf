from models import User
from tweets import get_tweets
from get_mbti import clean_text, get_result
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier


search_name = 'theweeknd'
tweets = get_tweets(search_name)
words = clean_text(tweets)
result = get_result(words)

print(result)