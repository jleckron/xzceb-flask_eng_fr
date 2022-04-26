import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testNull(self):
        self.assertNotEqual(english_to_french(" "), "")

    def testHello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def testNull(self):
        self.assertNotEqual(french_to_english(" "), "")

    def testHello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()