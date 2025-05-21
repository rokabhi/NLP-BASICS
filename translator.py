from translate import Translator

def translate_text(text, from_lang, to_lang):
    """
    Translates the given text from the source language to the target language.
    
    :param text: The text to translate.
    :param from_lang: The source language code (e.g., 'en' for English, 'la' for Latin).
    :param to_lang: The target language code (e.g., 'es' for Spanish, 'fr' for French).
    :return: The translated text.
    """
    try:
        # Create a Translator object
        translator = Translator(from_lang='en', to_lang=to_lang)
        # Translate the text
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"An error occurred: {e}"

def main():
	print("Welcome to the Language Translator! enter exit to exit")
	while (True):
		# Input text to translate
		text = input("Enter the text you want to translate: ")
		if text.lower() == 'exit' : exit(0)
		# Input source and target languages
		from_lang = input("Enter the source language code (e.g., 'en' for English, 'la' for Latin): ")
		to_lang = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ")

		# Translate the text
		translated_text = translate_text(text, from_lang, to_lang)

		# Display the result
		print("\nTranslated Text:")
		print(translated_text)

if __name__ == "__main__":
    main()
