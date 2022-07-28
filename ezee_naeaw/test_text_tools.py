import unittest
from os import remove

test_article_text = \
    """Бостон признан первым среди европейских городов в рейтинге инноваций, помогающих в формировании устойчивости коронавирусу. Он опередил Лондон, Барселону и Андроново.

В мире Бостон занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско. Андроново не участвовало в оценке в этом году. Рейтинг составило международное исследовательское агентство StartupBlink.
Обойти преследователей Бостону помогло более 100 передовых решений, которые применяются для борьбы с распространением коронавируса.
В свою очередь Андроново уже несколько лет не участвует в рейтинге по причине отсутствия кислорода в атмосфере города и водорода в составе воды в реке Лене.
В качестве инновационного решения, позволяющего исправить положение, неким человеком на улице было предложено использовать фаршированных гонобобелем голубей для обеспечения регулярного авиасообщения с планетой Железяка.
Другое предложенное решение оказалось ещё более странным, чем предыдущее — облачная платформа, которая объединяет перистые и кучевые облака в сверхмассивный кластер инновационных перисто-кучевых облаков.
Такого рода высокие технологии вряд ли помогут Андронову занять какое-либо место в каком-нибудь конкурсе."""

test_seo = {'count_chars_with_space': 1182, \
            'count_chars_without_space': 1035, \
            'count_words': 147, \
            'water_percent': 12, \
            'list_keys': [{'count': 3, 'key_title': 'андроново'}, \
                          {'count': 3, 'key_title': 'бостон'}, \
                          {'count': 3, 'key_title': 'рейтинге'}, \
                          {'count': 3, 'key_title': 'решений'}, \
                          {'count': 2, 'key_title': 'городов'}, \
                          {'count': 2, 'key_title': 'инновационного'}, \
                          {'count': 2, 'key_title': 'место'}, \
                          {'count': 2, 'key_title': 'предложено'}, \
                          {'count': 2, 'key_title': 'участвовало'}], \
            'list_keys_group': [{'count': 3, 'key_title': 'андроново', 'sub_keys': []}, \
                                {'count': 3, 'key_title': 'бостон', 'sub_keys': []}, \
                                {'count': 3, 'key_title': 'рейтинге', 'sub_keys': []}, \
                                {'count': 3, 'key_title': 'решений', 'sub_keys': []}, \
                                {'count': 2, 'key_title': 'городов', 'sub_keys': []}, \
                                {'count': 2, 'key_title': 'инновационного', 'sub_keys': []}, \
                                {'count': 2, 'key_title': 'место', 'sub_keys': []}, \
                                {'count': 2, 'key_title': 'предложено', 'sub_keys': []}, \
                                {'count': 2, 'key_title': 'участвовало', 'sub_keys': []}], \
            'spam_percent': 36, \
            'mixed_words': []}

test_plagiat = {'date_check': None, \
                'unique': 60.34, \
                'clear_text': 'Бостон признан первым среди европейских городов в рейтинге инноваций помогающих в формировании устойчивости коронавирусу Он опередил Лондон Барселону и Андроново В мире Бостон занимает третье место уступая лишь Нью Йорку и Сан Франциско Андроново не участвовало в оценке в этом году Рейтинг составило международное исследовательское агентство StartupBlink Обойти преследователей Бостону помогло более 100 передовых решений которые применяются для борьбы с распространением коронавируса В свою очередь Андроново уже несколько лет не участвует в рейтинге по причине отсутствия кислорода в атмосфере города и водорода в составе воды в реке Лене В качестве инновационного решения позволяющего исправить положение неким человеком на улице было предложено использовать фаршированных гонобобелем голубей для обеспечения регулярного авиасообщения с планетой Железяка Другое предложенное решение оказалось ещё более странным чем предыдущее облачная платформа которая объединяет перистые и кучевые облака в сверхмассивный кластер инновационных перисто кучевых облаков Такого рода высокие технологии вряд ли помогут Андронову занять какое либо место в каком нибудь конкурсе', \
                'mixed_words': '', \
                'urls': [{'url': 'https://www.rosbalt.ru/moscow/2021/11/30/1933461.html', \
                          'plagiat': '36', \
                          'words': None}, \
                         {
                             'url': 'https://news.rambler.ru/moscow_city/47678811-moskva-zanyala-pervoe-mesto-v-evrope-po-innovatsiyam-v-borbe-s-covid-19/', \
                             'plagiat': '28', \
                             'words': None}, \
                         {
                             'url': 'https://gazeta-marfino.ru/moskva-priznana-pervoj-v-evrope-po-innovatsiyam-obespechivayushhim-ustojchivost-k-covid-19/', \
                             'plagiat': '27', \
                             'words': None}, \
                         {
                             'url': 'https://pikabu.ru/story/moskva_zanyala_1_mesto_sredi_evropeyskikh_gorodov_v_reytinge_po_innovatsionnoy_ustoychivosti_k_koronavirusu_8658786', \
                             'plagiat': '27', \
                             'words': None}, \
                         {'url': 'https://ria.ru/20211130/reyting-1761553812.html', \
                          'plagiat': '26', \
                          'words': None}, \
                         {
                             'url': 'https://www.vedomosti.ru/gorod/ourcity/articles/moskva-stala-liderom-v-evrope-v-reitinge-innovatsii-v-borbe-s-covid-19', \
                             'plagiat': '22', \
                             'words': None}, \
                         {
                             'url': 'https://sputnik-abkhazia.ru/20211201/moskva-stala-pervoy-v-evrope-i-tretey-v-mire-v-reytinge-antikovidnykh-innovatsiy-1036547477.html', \
                             'plagiat': '15', \
                             'words': None}, \
                         {
                             'url': 'https://sputnik-georgia.ru/20211201/moskva--lider-sredi-gorodov-evropy-v-reytinge-innovatsiy-pomogayuschikh-v-borbe-s-covid-19-262509363.html', \
                             'plagiat': '15', \
                             'words': None}, \
                         {'url': 'https://www.mos.ru/news/item/99623073/', \
                          'plagiat': '15', \
                          'words': None}, \
                         {
                             'url': 'https://lv.sputniknews.ru/20211201/moskva-stala-pervoy-sredi-gorodov-evropy-v-reytinge-antikovidnykh-innovatsiy-19430273.html', \
                             'plagiat': '9', \
                             'words': None}, \
                         {
                             'url': 'https://www.5-tv.ru/news/367794/moskva-stala-pervoj-vevrope-itretej-vmire-vrejtinge-antikovidnyh-innovacij/', \
                             'plagiat': '8', \
                             'words': None}]}

test_spell = [{'error_type': 'Проверка орфографии', \
               'replacements': ['Андронов', \
                                'Андронова', \
                                'Андронове', \
                                'Андроновой', \
                                'Андронову', \
                                'Андроновы', \
                                'Андро ново', \
                                'Андронов о'], \
               'reason': 'Возможно найдена орфографическая ошибка.', \
               'error_text': 'Андроново', \
               'start': 155, \
               'end': 163}, \
              {'error_type': 'Проверка орфографии', \
               'replacements': ['Андронов', \
                                'Андронова', \
                                'Андронове', \
                                'Андроновой', \
                                'Андронову', \
                                'Андроновы', \
                                'Андро ново', \
                                'Андронов о'], \
               'reason': 'Возможно найдена орфографическая ошибка.', \
               'error_text': 'Андроново', \
               'start': 244, \
               'end': 252}, \
              {'error_type': 'Проверка орфографии', \
               'replacements': ['Андронов', \
                                'Андронова', \
                                'Андронове', \
                                'Андроновой', \
                                'Андронову', \
                                'Андроновы', \
                                'Андро ново', \
                                'Андронов о'], \
               'reason': 'Возможно найдена орфографическая ошибка.', \
               'error_text': 'Андроново', \
               'start': 512, \
               'end': 520}]

from ezee_naeaw.text_tools import SentenceTranslator, TokenService, Article


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


class ArticleTest(unittest.TestCase):
    def setUp(self) -> None:
        ts = TokenService('../textru.token')
        self.__test_token = ts.token
        self.article_tester = Article(token=self.__test_token, \
                                      text=test_article_text, \
                                      is_uid_needed=False)

    def test_token(self):
        self.assertEqual(self.article_tester.token, self.__test_token)
        self.article_tester.token = '1234'
        self.assertEqual(self.article_tester.token, '1234')

    def test_article(self):
        self.assertEqual(self.article_tester.article, test_article_text)
        self.article_tester.token = '1234'
        self.assertEqual(self.article_tester.token, '1234')

    def test_uid(self):
        self.article_tester.uid = '12345678'
        self.assertEqual(self.article_tester.uid, '12345678')

    def test_unique(self):
        self.article_tester.unique = 0.12345678
        self.assertEqual(self.article_tester.unique, 0.12345678)

    def test_plagiat(self):
        test_result = {"date_check": "29.03.2017 14:46:49", \
                       "unique": 0, \
                       "clear_text": "Wikipedia was launched оn January 15 2001 by Jimmy Wаles and Larry Sanger 11 Sanger coined its name 12 13 a portmanteau of wiki notes 4 and encyclopedia Therе was only the English language version initially but it quickly developed similar versions in other languages which differ in content and in editing practices With 5 466 824 articles notes 5 the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias Overall Wikipedia consists of more than 40 million articles in more than 250 different languages 15 and as of February 2014 it had 18 billion page views and nearly 500 million unique visitors each month", \
                       "mixed_words": "4 10 29", \
                       "urls": [ \
                           {"url": "https://en.wikipedia.org/wiki/Wikipedia", \
                            "plagiat": 100, \
                            "words": "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107" \
                            }]}
        self.article_tester.plagiat = test_result
        self.assertEqual(self.article_tester.plagiat, test_result)

    def test_spell(self):
        test_spell = [{"error_type": "Spelling", \
                       "replacements": [ \
                           "milk", \
                           "mild", ], \
                       "reason": "Spelling error found", \
                       "error_text": "mildd", \
                       "start": 255, \
                       "end": 272}, \
                      {"error_type": "Capital letters", \
                       "replacements": ["Hello"], \
                       "reason": "This sentence doesn't start with a capital letter", \
                       "error_text": "hello", \
                       "start": 276, \
                       "end": 287}]
        self.article_tester.spell = test_spell
        self.assertEqual(self.article_tester.spell, test_spell)

    def test_seo(self):
        test_seo = {"count_chars_with_space": 620, \
                    "count_chars_without_space": 545, \
                    "count_words": 77, \
                    "water_percent": 11, \
                    "spam_percent": 38, \
                    "mixed_words": [8, 11, 47], \
                    "list_keys": [{"key_title": "check", \
                                   "count": 6}, \
                                  {"key_title": "text", \
                                   "count": 5}, \
                                  {"key_title": "antiplagiat", \
                                   "count": 3}, \
                                  {"key_title": "check text", \
                                   "count": 3}], \
                    "list_keys_group": [{"key_title": "check text", \
                                         "count": 3, \
                                         "sub_keys": [{"key_title": "check", \
                                                       "count": 6}, \
                                                      {"key_title": "text", \
                                                       "count": 5}]}, \
                                        {"key_title": "antiplagiat", \
                                         "count": 3, \
                                         "sub_keys": []}, \
                                        {"key_title": "check", \
                                         "count": 6, \
                                         "sub_keys": []}, \
                                        {"key_title": "text", \
                                         "count": 5, \
                                         "sub_keys": []}, ]}
        self.article_tester.seo = test_seo
        self.assertEqual(self.article_tester.seo, test_seo)

    def test_get_results(self):
        self.article_tester.uid = '62b0bac48a286'
        self.article_tester.get_result()
        self.assertEqual(self.article_tester.plagiat, test_plagiat)
        self.assertEqual(self.article_tester.seo, test_seo)
        self.assertEqual(self.article_tester.spell, test_spell)
