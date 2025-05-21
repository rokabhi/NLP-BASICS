import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

class TextClassifier:
    def __init__(self):
        # Initialize VADER sentiment analyzer
        self.sid = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess_text(self, text):
        """Preprocess the text by tokenizing, removing stopwords, and lemmatizing"""
        # Tokenize
        tokens = word_tokenize(text.lower())
        # Remove stopwords and non-alphabetic tokens
        tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        # Lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(tokens)
    
    def get_sentiment(self, text):

        scores = self.sid.polarity_scores(text)
       
        compound_score = scores['compound']
        
        if compound_score >= 0.05:
            return 'positive', scores
        elif compound_score <= -0.05:
            return 'negative', scores
        else:
            return 'neutral', scores
    
    def classify_text(self, text):
        """Classify text and return detailed results"""
        # Preprocess the text
        processed_text = self.preprocess_text(text)
        
        # Get sentiment
        sentiment, scores = self.get_sentiment(text)
        
        return {
            'original_text': text,
            'processed_text': processed_text,
            'sentiment': sentiment,
            'scores': {
                'positive': scores['pos'],
                'negative': scores['neg'],
                'neutral': scores['neu'],
                'compound': scores['compound']
            }
        }

# Example usage
if __name__ == "__main__":
    classifier = TextClassifier()
    custom_text = input('Enter the Text :')
    result = classifier.classify_text(custom_text)
    print(f"Custom Text Analysis:")
    print(f"Text: {custom_text}")
    print(f"Sentiment: {result['sentiment'].upper()}")
    print(f"Compound Score: {result['scores']['compound']:.3f}")
