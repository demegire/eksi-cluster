from googletrans import Translator

translator = Translator()

def translateObject(text, src_lang, dest_lang):
    translation = translator.translate(text, src=src_lang, dest=dest_lang)        
    return translation.text    

# a = translateObject("lütfen araçları hızlı kullanmayın. lütfen kendinize güvenmeyin. yağışlı havalarda hiç sürat yapmayın. direksiyon hakimiyetini kaybediyor. orada arıza yapan aracın suçu ne? çok ama çok yazık. boş yere giden 4 can. 2 kişide ağır yaralı...", "tr", "en")
# print(a)
