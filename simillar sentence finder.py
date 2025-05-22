'''

try:
	with open ("/home/dell/abhijith/text3.txt","r") as file:
		text =  file.read()
except : 
	print("file not found")
	
from collections import Counter
from nltk.tokenize import sent_tokenize,word_tokenize 
import re
import heapq
from sklearn.metrics.pairwise import cosine_similarity
import string



corpus = text.split('.')
text = text.translate(str.maketrans('','',string.punctuation))

print(text)

'''

import nltk

from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import heapq
from sklearn.metrics.pairwise import cosine_similarity

# Ensure 'text' is defined even if file is not found
text = ""
try:
    with open("/home/dell/abhijith/text3.txt", "r") as file:
        text = file.read()
except:
    print("file not found")

# Tokenizing sentences
sentences = sent_tokenize(text.lower())

corpus = []
words = []
for sentence in sentences:
    sentence = re.sub(r'\W', ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    tokenized_sentence = word_tokenize(sentence)
    corpus.append(tokenized_sentence)
    words.extend(tokenized_sentence)

word_count = Counter(words)
stop_words = set(stopwords.words('english'))
# Filter out stopwords before sorting
filtered_words = {word: count for word, count in word_count.items() if word not in stop_words}

# Sort by frequency (descending)
sorted_dict = dict(sorted(filtered_words.items(), key=lambda item: item[1], reverse=True))

# Take the top 20 frequent words
freq_words = list(sorted_dict.keys())[:20]

print(freq_words)



# Creating sentence vectors
X = []
for sentence in corpus:
    vector = []
    count = Counter(sentence)
    for i in freq_words:
        vector.append(count[i] if i in count else 0)
    X.append(vector)

# Processing input text
input_text = input("Enter text: ").lower()
input_text = re.sub(r'\W', ' ', input_text)
input_text = re.sub(r'\s+', ' ', input_text)

vector = []
count = Counter(input_text.split())
w = set(word_tokenize(input_text))
for i in freq_words:
    vector.append(count[i] if i in w else 0)

X.insert(0, vector)

# Compute cosine similarity
cos_sim_matrix = cosine_similarity(X)

# Find most similar sentence
max_index = -1
max_similarity = 0
for i in range(1, len(cos_sim_matrix)):  # Fixed range
    if cos_sim_matrix[0][i] > max_similarity:
        max_similarity = cos_sim_matrix[0][i]
        max_index = i

# Print results
print("Input Vector:", X[0])
print("=" * 10)
'''
for i in range(1, len(X)):  # Adjusting index for printing
    print("Vector:", X[i])
    print("Sentence:", sentences[i - 1])  # Adjusted index
'''
if max_index != -1:
    print("Most Similar Sentence:", sentences[max_index - 1])
    print("Cosine Similarity:", max_similarity)

