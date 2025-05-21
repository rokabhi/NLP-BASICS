
import re
# Import the required module
from sklearn.feature_extraction.text import TfidfVectorizer
# Assign documents
d1 = 'Elon Musk founded SpaceX in 2002 in California.'
d2='Apple Inc released the iPhone 13 on September 24 2021.' 
d3 ='Barack Obama was the 44th President of the United States.' 
d4 = 'The FIFA World Cup 2022 was held in Qatar'
# Merge documents into a single corpus
string = [d1, d2, d3,d4]
# Create a TfidfVectorizer object
tfidf = TfidfVectorizer()
# Fit and transform the documents
result = tfidf.fit_transform(string)
# Get feature names
feature_names = tfidf.get_feature_names_out()
# Get idf values
idf_values = tfidf.idf_
# Print idf values
import pandas as pd
tfidf_matrix = result.toarray()
# Create a DataFrame for a nicer display, with words as column headers
df = pd.DataFrame(tfidf_matrix, columns=feature_names)
# Print the table
print(df)

	
	
			
