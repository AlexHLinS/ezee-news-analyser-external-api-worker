from datetime import datetime

import requests

class BlackList(object):
    def __init__(self):
        self.__init_datetime = datetime.datetime.now()
        pass

    def update_blacklist(self):
        pass