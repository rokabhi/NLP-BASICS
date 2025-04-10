import re
from collections import Counter

def tokenize_tweets(tweets):
    sentences = tweets.split('.')
    words = []
    for sentence in sentences:
        for word in sentence.split():
            words.append(word)
    return words
def to_lower(tokenized_tweets):
    lower_tweets=[word.lower() for word in tokenized_tweets]
    return lower_tweets

def remove_punct(tweets):
    punct_removed_tweets = [re.sub(r'[^\w\s]', '', word) for word in tweets]
    return [word for word in punct_removed_tweets if word]

with open("/home/dell/JOEL_S6/data2.txt","r") as f:
     sentences=f.read()
f.close()

words=tokenize_tweets(sentences)

words=to_lower(words)
words=remove_punct(words)
words.sort()

print(f'No.of Words/Tokens : {len(words)}')
print(f'No of unique words : {len(Counter(words))}')
for x in Counter(words):
    print(f"{x}-{Counter(words)[x]}-{round(float(Counter(words)[x]/len(words)),2)}%")
    print()
    with open("output.txt","a") as f:
         f.write(f"{x}-{Counter(words)[x]}-{round(float(Counter(words)[x]/len(words)),2)}%")
         f.write("\n")
    f.close()
print("Saved to output.txt")

