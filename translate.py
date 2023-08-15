from googletrans import Translator

translator = Translator()

def translate(text):
    text = text[:1000]
    try: # Translation service might not be always reliable
        translation = translator.translate(text, src='tr', dest='en')
        translation = translation.text
    except Exception as e:
        print(e)
        translation = 'Translation error'        
    return translation