import unittest
from os import remove

from text_tools import SentenceTranslator, TokenService


class SentanceTranslatorTester(unittest.TestCase):
    def setUp(self) -> None:
        self.test_sentence_translator = SentenceTranslator('привет', 'ru', 'en')

    def test_original_sentence(self) -> None:
        self.assertEqual(self.test_sentence_translator.original_sentences, 'привет')
        self.test_sentence_translator.original_sentences = 'hello'
        self.assertEqual(self.test_sentence_translator.original_sentences, 'hello')

    def test_from_language(self) -> None:
        self.assertEqual(self.test_sentence_translator.from_lang, 'ru')
        self.test_sentence_translator.from_lang = 'en'
        self.assertEqual(self.test_sentence_translator.from_lang, 'en')

    def test_to_language(self) -> None:
        self.assertEqual(self.test_sentence_translator.to_lang, 'en')
        self.test_sentence_translator.to_lang = 'ru'
        self.assertEqual(self.test_sentence_translator.to_lang, 'ru')

    def test_sentence_translator(self):
        self.assertEqual(self.test_sentence_translator.translate(), 'hi ')

    def test_translated_sentence(self) -> None:
        self.test_sentence_translator.translate()
        self.assertEqual(self.test_sentence_translator.translated_sentences, 'hi ')
        with self.assertRaises(AttributeError):
            self.test_sentence_translator.translated_sentences = 'test'


class TokenServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_token = 'testtokenstring\n'
        self.__test_token_file_name = 'test.token'
        with open(self.__test_token_file_name, 'w') as test_token_file:
            test_token_file.write(self.__test_token)
        self.test_token_service = TokenService(self.__test_token_file_name)

    def test_get_token_from_file(self) -> None:
        self.assertEqual(self.test_token_service.get_token_from_file(), self.__test_token.replace('\n', ''))

    def test_token(self) -> None:
        self.test_token_service.token = '1234'
        self.assertEqual(self.test_token_service.token, '1234')

    def tearDown(self) -> None:
        try:
            remove('test.token')
        except FileNotFoundError:
            pass



