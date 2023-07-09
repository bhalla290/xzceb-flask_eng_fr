""" This file is for my translator """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ This function is for translating english to french """
    #write the code here
    translator = MyMemoryTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """ This function is for translating french to english """
    #write the code here
    translator = MyMemoryTranslator(source='french', target='english')
    english_text = translator.translate(french_text)
    return english_text
