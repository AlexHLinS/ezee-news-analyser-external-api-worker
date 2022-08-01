from datetime import datetime
from typing import List
from newspaper import Article
from htmldate import find_date
import requests
import numpy as np
from datetime import datetime


class UrlCreationDataGetter:
    def __init__(self, urls: List):
        self.urls = urls
        pass

    @staticmethod
    def get_date_from_newspaper(url: str) -> str:
        article = Article(url, language='ru')
        article.download()
        article.parse()
        article.nlp()
        return article.publish_date[:10]

    @staticmethod
    def get_date_from_find_date(url: str) -> str:
        return find_date(requests.get(url=url).text)

    def get_dates(self) -> List:
        """
        :return: list of dates or NaTs
        """
        tmp_list = list()
        for url in self.urls:
            tmp_list.append([url, self.get_date_from_find_date(url), self.get_date_from_newspaper(url)])
        df = pd.DataFrame(data=tmp_list, columns=['urls', 'get_date', 'newspaper'])
        df['result'] = pd.to_datetime(np.where(df['newspaper'].isna(), df['get_date'], df['newspaper']), utc=True)
        result = df['result'].to_list()
        return result


class BlackList(object):
    def __init__(self):
        self.__init_datetime = datetime.now()
        pass

    def update_blacklist(self):
        pass
