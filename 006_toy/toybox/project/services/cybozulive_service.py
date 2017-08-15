#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

from logging import getLogger
logger = getLogger(__name__)

# ----------
# cybozulive
# ----------
import oauth2
import urllib

ACCESS_TOKEN_URL = 'https://api.cybozulive.com/oauth/token'
GROUP_ID_URL = 'https://api.cybozulive.com/api/group/V2'

CONSUMER_TOKEN = {
    'key': 'dddd',
    'secret': 'aaaa'
}

USER_ACCOUNT = {
    'username': 'gggg',
    'password': 'rrggg',
    'mode': 'client_auth'
}

# ----------
# simpleApi
# ----------
HOST = "news.yahoo.co.jp"
PORT = "80"
PATH = '/pickup/sports/rss.xml'
DEFAULT_HEADERS = {'Content-Type': 'application/json'}


class CybozuliveService():

    access_token = {}

    @classmethod
    def post_message_bulletin_board(CybozuliveService):
        """サイボウズLiveの掲示板にメッセージを投稿する関数
        """

        logger.info('-- START ---')

        result = CybozuliveService.get_access_token()

        result = CybozuliveService.get_group_id()

        logger.info('-- END ---')

        return result

    @classmethod
    def get_access_token(CybozuliveService):
        """サイボウズLiveの認証トークンを取得する関数
        """

        logger.info('-- START ---')

        result = {}
        result['oauth_token'] = ''
        result['oauth_token_secret'] = ''

        try:
            consumer = oauth2.Consumer(
                CONSUMER_TOKEN['key'], CONSUMER_TOKEN['secret'])
            client = oauth2.Client(consumer)
            client.add_credentials(
                USER_ACCOUNT['username'], USER_ACCOUNT['password'])
            client.authorizations

            params = {}
            params["x_auth_username"] = USER_ACCOUNT['username']
            params["x_auth_password"] = USER_ACCOUNT['password']
            params["x_auth_mode"] = USER_ACCOUNT['mode']

            client.set_signature_method = oauth2.SignatureMethod_HMAC_SHA1()
            resp, token = client.request(
                ACCESS_TOKEN_URL, method="POST", body=urllib.parse.urlencode(params))

            logger.info(resp)

            if resp['status'] is 200:
                # oauth_token        : xxxxx
                # oauth_token_secret : xxxxx
                result = urllib.parse.parse_qs(token)
                CybozuliveService.access_token = urllib.parse.parse_qs(token)

        except Exception as e:
            CybozuliveService.access_token = result
            return result

        logger.info('-- END ---')

        return result

    @classmethod
    def get_group_id(CybozuliveService, group_name='自分用グループ'):
        """サイボウズLiveの対象のグループのグループIDを取得する関数
        """
        logger.info('-- START ---')

        result = CybozuliveService.get_access_token()

        logger.info('-- END ---')
        return result

    def simple_api():
        """getリクエストで単純取得できるRSSの動作確認用
        """

        try:
            return requests.get("http://{0}:{1}{2}".format(HOST, PORT, PATH),
                                params={},
                                headers=DEFAULT_HEADERS)

        except Exception as e:
            return None
