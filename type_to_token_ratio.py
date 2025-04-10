try:
	with open('/home/dell/abhijith/text1.txt','r') as file:
		text = file.read()
except Exception as e:
    print(f"An error occurred: {e}")
	

import string
import re
import nltk

#text = text.translate(str.maketrans('','',string.punctuation))
text = re.sub(r'[^\w\s]','',text)
print(text)

from nltk.tokenize import sent_tokenize, word_tokenize

text = word_tokenize(text)

noof = len(text)
print(f'number of words = {noof}')


from collections import Counter
count = Counter(text)
dword = len(set(text))
#dword = len(count)
print(f'number of different words {dword}')

ll=[]
for i,j in count.items():
	ll.append(i)
	print(f'occurance of {i} = {j}')
	print(f'percentage of {i} is {(j/noof)*100}')
	
	print('*'*10)
print(ll)
print(f'type to token ratio of = {(dword/noof)*100}')




