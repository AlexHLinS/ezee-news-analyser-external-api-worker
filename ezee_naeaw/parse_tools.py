from newspaper import Article


def parse_web_article(url):
    """
    :param url: Адрес статьи
    :return: кортеж (<заголовок_статьи>, <текст_статьи>)
    """

    article = Article(url=url)
    article.download()
    article.parse()

    return article.title, article.text
