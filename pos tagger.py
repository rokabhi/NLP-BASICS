import nltk
from nltk import word_tokenize , pos_tag , ne_chunk
text = input("enter the input text ").upper()
tokens = word_tokenize(text)

tagged = pos_tag(tokens)
ner_tree = ne_chunk(tagged)

named_entity = []

for subtree in ner_tree :
	if isinstance(subtree,nltk.Tree):
		entity_name  = " ".join(word for word , tag in subtree.leaves())
		entity_type  = subtree.label()
		named_entity.append((entity_name,entity_type))

print("\nExtracted Named Entities:")
for entity, entity_type in named_entity:
    print(f"{entity}: {entity_type}")


