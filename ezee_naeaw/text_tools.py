from typing import Dict

from slovnet.sent import sentenize
from translate import Translator


class SentenceTranslator:
    """
    This class implements object of translation for given sentence
    and directions
    """

    def __init__(self, sentence: str, from_lang: str = 'en', to_lang: str = 'ru'):
        self.__translated_sentences = None
        self.__original_sentences = sentence
        self.__from_lang = from_lang
        self.__to_lang = to_lang

    @property
    def original_sentences(self):
        return self.__original_sentences

    @original_sentences.setter
    def original_sentences(self, sentence):
        self.__original_sentences = sentence
        self.translate()

    @property
    def from_lang(self):
        return self.__from_lang

    @from_lang.setter
    def from_lang(self, lang: str):
        self.__from_lang = lang
        self.translate()

    @property
    def to_lang(self):
        return self.__to_lang

    @to_lang.setter
    def to_lang(self, lang: str):
        self.__to_lang = lang
        self.translate()

    @property
    def translated_sentences(self):
        return self.__translated_sentences

    @translated_sentences.setter
    def translated_sentences(self, value: str):
        raise AttributeError('This is a read-only property!')

    def translate(self) -> str:
        """
        Started translation process
        :return: Translation results, or None if not available
        """
        result = ''
        sentences = list(sentenize(self.__original_sentences))
        for sentence in sentences:
            translator = Translator(from_lang=self.__from_lang, to_lang=self.__to_lang)
            result = result + translator.translate(sentence.text) + ' '
        self.__translated_sentences = result
        return self.get_translated_text()

    def get_translated_text(self) -> str | None:
        """
        Getter for translated_sentences field
        :return: Translation results, or None if not available
        """
        return self.__translated_sentences

    def get_original_text(self) -> str | None:
        """
        Getter for original_sentences field
        :return: Original sentence, or None if not available
        """
        return self.__translated_sentences


class TokenService:
    """
    Implement TokenService class- a set of methods
    to get and store token information
    """

    def __init__(self, token_file_path: str):
        self.__token_file_path = token_file_path
        self.__token = None
        self.get_token_from_file()

    def get_token_from_file(self) -> str | None:
        """
        :return: token, or None if not available
        """
        with open(self.__token_file_path, 'r') as token_file:
            token = token_file.readline().replace('\n', '')
        if not token or len(token) < 1:
            raise ValueError('Provided file has no token!')
        self.token = token
        return self.token

    @property
    def token(self) -> str | None:
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value


class Article:
    api_request_url = 'https://api.text.ru/post'

    def __init__(self, token: str, text: str) -> str:
        self.__token = token
        self.__text = text
        self.__uid = None
        self.__text_unique = None
        self.__antiplag_results = None
        self.__spell_results = None
        self.__seo_results = None

    @property
    def token(self) -> str | None:
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @property
    def article(self) -> str | None:
        return self.__text

    @article.setter
    def article(self, value: str):
        self.__text = value

    @property
    def uid(self) -> str | None:
        return self.__uid

    @uid.setter
    def uid(self, value: str):
        self.__uid = value

    @property
    def unique(self) -> float | None:
        return self.__text_unique

    @unique.setter
    def unique(self, value: float):
        self.__text_unique = value

    @property
    def plagiat(self) -> Dict | None:
        return self.__antiplag_results

    @plagiat.setter
    def plagiat(self, value:Dict):
        self.__antiplag_results = value

    @property
    def spell(self) -> Dict | None:
        return self.__spell_results

    @spell.setter
    def spell(self, value: Dict):
        self.__spell_results = value

    @property
    def seo(self):
        return self.__seo_results

    @seo.setter
    def seo(self, value: Dict):
        self.__seo_results = value

    # TODO: Implement text.ru API interface worker