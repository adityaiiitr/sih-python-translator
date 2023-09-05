from googletrans import Translator

def translateText(text, source_lang, target_lang):
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text

    except Exception as e:
        return f"Translation error: {str(e)}"
