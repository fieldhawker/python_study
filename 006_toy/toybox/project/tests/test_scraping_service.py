# -*- coding: utf-8 -*-

import sys,os

import unittest
from unittest import mock

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../services')
import scraping_service


class TestScrapingService(unittest.TestCase):

    # helloworld.
    def test_main(self):

        url = 'https://news.google.com/news/?ned=jp&hl=ja'

        # result = scraping_service.ScrapingService.get_link(url)
        # print(result)

if __name__ == "__main__":
    unittest.main()
