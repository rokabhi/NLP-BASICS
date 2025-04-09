import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import contractions
import string
from nltk.stem import PorterStemmer

try:
     with open("data1.txt","r") as f:
         tweets=f.read()
     
     f.close()
except Exception as e:
      print(e)
def remove_urls(tweets):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub("", tweets)

def replace_contractions(tweets):
    return contractions.fix(tweets)

def tokenize_tweets(tweets):
    return word_tokenize(tweets)

def to_lower(tokenized_tweets):
    return [word.lower() for word in tokenized_tweets]

def remove_punct(tokens):
    return [word for word in tokens if word not in string.punctuation]

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

def stemming(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]

def lemmatization(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]
def remove_emoji(tweets):
    emoji_pattern = re.compile(
        "[\U00010000-\U0010ffff"  # Emojis
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub("", tweets)

print(f"Original Tweet: {tweets}")

print(f"Sentence tokenizing: {sent_tokenize(tweets)}")

tweets=remove_emoji(tweets)
print(f"After Removing emoji : {tweets}")
tweets = remove_urls(tweets)
print(f"After Removing URLs: {tweets}")

tweets = replace_contractions(tweets)
print(f"After Expanding Contractions: {tweets}")

tokenized_tweets = tokenize_tweets(tweets)
print(f"Tokenized Tweets: {tokenized_tweets}")

lower_tokens = to_lower(tokenized_tweets)
print(f"Lowercase Tokens: {lower_tokens}")

no_punct_tokens = remove_punct(lower_tokens)
print(f"Tokens After Removing Punctuation: {no_punct_tokens}")

no_stopwords_tokens = remove_stopwords(no_punct_tokens)
print(f"Tokens After Removing Stopwords: {no_stopwords_tokens}") 

stemmed_tokens = stemming(no_stopwords_tokens)
print(f"Tokens After Stemming: {stemmed_tokens}")

lemmatized_tokens = lemmatization(no_stopwords_tokens)
print(f"Tokens After Lemmatization: {lemmatized_tokens}")


