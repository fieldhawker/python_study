# coding utf-8

import pprint
import requests

from time import sleep


def remove_cache():

    # ファイル名
    read  = 'Googlebot.txt'
    write = 'Googlebot2.txt'

    # 非表示文字
    newline = '\n'

    # 接続先サーバ
    # url = 'http://127.0.0.1:5000/get'
    # url = 'http://frontpc.local/product/removehistory/id_'

    # リクエスト周期(s)
    second = 0.1

    w = open(write, 'wb')

    with open(read) as lines:

        for line in lines:

            # 対象文字列
            pprint.pprint(line)

            # URL
            # url = url + line.rstrip(newline)

            # GETリクエスト
            # response = requests.get(url)

            # pprint.pprint(response)

            # GET
            response = requests.get(
                'http://127.0.0.1:5000/get',
                {'foo': 'bar'})

            pprint.pprint(response.json())

            # POST
            # response = requests.post(
            #     'http://127.0.0.1:5000/post',
            #     {'foo': 'bar'})
            #
            # pprint.pprint(response.json())

            # 実行した文字列をログに出力
            w.write(line.encode('utf-8'))

            # リクエスト周期
            sleep(second)

    w.close()


if __name__ == '__main__':
    remove_cache()

# input()
