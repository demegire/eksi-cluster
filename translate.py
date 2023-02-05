from googletrans import Translator

translator = Translator()

def translate(text):
    translation = translator.translate(text, src='tr', dest='en')        
    return translation.text    

# a = translateObject("lütfen araçları hızlı kullanmayın. lütfen kendinize güvenmeyin. yağışlı havalarda hiç sürat yapmayın. direksiyon hakimiyetini kaybediyor. orada arıza yapan aracın suçu ne? çok ama çok yazık. boş yere giden 4 can. 2 kişide ağır yaralı...", "tr", "en")
# print(a)
