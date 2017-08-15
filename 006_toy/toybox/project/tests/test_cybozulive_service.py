#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import mock

from services.cybozulive_service import CybozuliveService


class TestCybozuliveService(TestCase):

    # helloworld.
    def test_helloworld(self):
        self.assertEqual('helloworld', 'helloworld')

    # post_message_bulletin_board.
    def test_post_message_bulletin_board(self):

        for i in range(0, 6):
            with self.subTest(i=i):
                with \
                        mock.patch('services.cybozulive_service.CybozuliveService.get_access_token', return_value='helloworld1') as m1, \
                        mock.patch('services.cybozulive_service.CybozuliveService.get_group_id', return_value=i) as m2:

                    self.assertEqual(
                        'helloworld1', CybozuliveService.post_message_bulletin_board())

    # APIをキックする場所なのでテストから除外
    # get_access_token.
    def test_get_access_token(self):
        with mock.patch(
            'services.cybozulive_service.CybozuliveService.get_access_token',
            return_value='helloworld'
        ) as patcher:

            self.assertEqual(
                'helloworld', CybozuliveService.get_access_token())

    # APIをキックする場所なのでテストから除外
    # get_group_id.
    def test_get_group_id(self):
        with mock.patch(
            'services.cybozulive_service.CybozuliveService.get_access_token',
            return_value='the result'
        ) as patcher:

            self.assertEqual('the result', CybozuliveService.get_group_id())

    # APIをキックするのでmockに置き換え
    # helloworld.
    def test_simple_api(self):
        with mock.patch(
            'services.cybozulive_service.CybozuliveService.simple_api',
            return_value='helloworld'
        ) as patcher:

            self.assertEqual('helloworld', CybozuliveService.simple_api())
