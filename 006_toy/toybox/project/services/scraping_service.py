# -*- coding: utf-8 -*-

import sys,os
import requests

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../toybox/toybox')

import settings
from bs4 import BeautifulSoup

from logging import getLogger
logger = getLogger(__name__)

class ScrapingService():

    def __init__():

        pass


    def get_link(url):

        logger.info('-- START ---')

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        result = []
        for a in soup.find_all('a'):
            result.append(a.get('href'))

        logger.info('-- END ---')

        return result
