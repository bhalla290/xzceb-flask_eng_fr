import unittest

from deep_translator import MyMemoryTranslator

class TranslatorTestCase(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "hello"
        expected_french_text = "bonjour"
        
        translator = MyMemoryTranslator(source='english', target='french')
        translated_text = translator.translate(english_text)
        
        self.assertEqual(translated_text, expected_french_text)
    
    def test_french_to_english(self):
        french_text = "bonjour"
        expected_english_text = "hello"
        
        translator = MyMemoryTranslator(source='french', target='english')
        translated_text = translator.translate(french_text)
        
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()