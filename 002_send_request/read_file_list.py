# coding utf-8

import os
import re
import pprint
import requests
import glob
import gzip
import zipfile
import fnmatch
import hashlib

from time import sleep

def remove_cache():
    """remove_cache()

    同一ディレクトリ内のgzファイルとzipファイルを検索し、
    圧縮ファイル内のテキストに記載されているキーからキャッシュキーを生成、
    okuyamaにキーに該当するキャッシュを削除する依頼を投げる（予定）
    """

    # リクエスト周期(s)
    second = 0.001
    # 非表示文字
    newline = '\n'

    # キーの生成ルール
    pre = ''
    sitecode = ''

    # 対象ファイルの抽出
    gz_list = glob.glob('./*.gz')
    z_list = glob.glob('./*.zip')

    # ---------------
    # gzファイル群
    # ---------------

    for gz_file in gz_list:

        # pprint.pprint(gz_file)
        name, ext = os.path.splitext(gz_file)
        # pprint.pprint(name)

        pre , sitecode = getPrefix(name)

        w = open(name + '.log', 'wb')

        if os.path.isfile(gz_file) == False:
            pprint.pprint('isfile : ' + gz_file + ' is not found')
            continue

        with gzip.open(gz_file, 'rt', "utf_8") as lines:

            for line in lines:
                key = line.rstrip(newline)
                if key != '' :
                    # 対象文字列
                    key = getCacheKey(pre, sitecode, key)

                    # ここでokuyamaに処理を投げる

                    w.write(line.encode('utf-8'))
                    # break

                # リクエスト周期
                sleep(second)

        w.close()

    # ---------------
    # zipファイル群
    # ---------------

    for z_file in z_list:

        # pprint.pprint(z_file)

        with zipfile.ZipFile(z_file, 'r') as file_list:

            for file_name in file_list.namelist():

                if fnmatch.fnmatch(file_name, '*.txt'):

                    pre , sitecode = getPrefix(file_name)

                    w = open(file_name + '.log', 'wb')
                    # pprint.pprint(file_name.rstrip(newline))

                    if os.path.isfile(file_name) == False:
                        pprint.pprint('isfile : ' + file_name + ' is not found')
                        continue

                    with open(file_name) as lines:

                        for line in lines:
                            key = line.rstrip(newline)
                            if key != '' :
                                # 対象文字列
                                key = getCacheKey(pre, sitecode, key)

                                # ここでokuyamaに処理を投げる

                                w.write(line.encode('utf-8'))
                                break

                            # リクエスト周期
                            sleep(second)

                    w.close()

def getPrefix(file_name):

    """getPrefix(file_name)

    ファイル名に含まれる文言によって、
    キャッシュキーを生成するプレフィックスとサイトコードを判定、
    結果を返す関数
    """

    if fnmatch.fnmatch(file_name, '*_shop_*'):
        pre = 'ors_'
    else:
        pre = 'orp_'

    if fnmatch.fnmatch(file_name, '*_mg*'):
        sitecode = '0000000000'
    else:
        sitecode = '0000000001'

    return (pre , sitecode)

def getCacheKey(pre, sitecode, key):

    """getCacheKey(pre, sitecode, key)

    引数を用いてキャッシュキーを生成、返却する変数
    """

    key = 'production_' + pre + \
        hashlib.md5((sitecode + key + 'ao1hz9dn').encode('utf-8')).hexdigest()
    pprint.pprint(key)

    return key


    # ファイルリスト
    # read_list = ['Googlebot.txt', 'Googlebot4.txt']
    # ファイル名
    # read  = 'Googlebot.txt'
    # write = 'Googlebot2.txt'
    # tar.gzファイル名
    # gz = '20170807_mgsp_shop_bot.txt.gz'
    # Zip ファイル名
    # z = '20161221_tstlog.zip'

    # 接続先サーバ
    # url = 'http://127.0.0.1:5000/get'
    # url = 'http://frontpc.local/product/removehistory/id_'

    # w = open(write, 'wb')

    # for read in read_list:
    #
    #     if os.path.isfile(read) == False:
    #         pprint.pprint('isfile : ' + read + ' is not found')
    #         continue
    #
    #     with open(read) as lines:
    #
    #         for line in lines:
    #
    #             # 対象文字列
    #             pprint.pprint(line)
    #
    #             # URL
    #             # url = url + line.rstrip(newline)
    #
    #             # GETリクエスト
    #             # response = requests.get(url)
    #
    #             # pprint.pprint(response)
    #
    #             # GET
    #             response = requests.get(
    #                 'http://127.0.0.1:5000/get',
    #                 {'foo': 'bar'})
    #
    #             pprint.pprint(response.json())
    #
    #             # POST
    #             # response = requests.post(
    #             #     'http://127.0.0.1:5000/post',
    #             #     {'foo': 'bar'})
    #             #
    #             # pprint.pprint(response.json())
    #
    #             # 実行した文字列をログに出力
    #             w.write(line.encode('utf-8'))
    #
    #             # リクエスト周期
    #             sleep(second)


    # w.close()

    # IF文の書き方
    # if os.path.isfile(read) == True:
    #     pprint.pprint('if : ' + read + ' is found')
    # elif os.path.isfile(read) == True:
    #     pprint.pprint('elif : ' + read + ' is not found')
    # else:
    #     pprint.pprint('else : ' + read + ' is not found')
    #
    # for文の書き方
    # for read in read_list:
    #     pprint.pprint('key : ' + 'x' + ' value : ' + read)

    # ファイルを行単位で読み込み
    # with open(read) as lines:
    #     for line in lines:

    # gzファイルを行単位で読み込み
    # with gzip.open(gz, 'rt', "utf_8") as file_list:
    #     for file_name in file_list:
    #         pprint.pprint(file_name.rstrip(newline))

# def file_read(file_name):

    # # 非表示文字
    # newline = '\n'
    #
    # # リクエスト周期(s)
    # second = 0.1
    #
    # pprint.pprint(file_name.rstrip(newline))
    #
    # if fnmatch.fnmatch(file_name, '*.txt'):
    #
    #     pprint.pprint(file_name.rstrip(newline))
    #
    #     if os.path.isfile(file_name) == False:
    #         pprint.pprint('isfile : ' + file_name + ' is not found')
    #         return
    #
    #     with open(file_name) as lines:
    #
    #         for line in lines:
    #             line = line.rstrip(newline)
    #             if line != '' :
    #                 # 対象文字列
    #                 pprint.pprint(line)
    #                 break
    #
    #             # リクエスト周期
    #             sleep(second)

if __name__ == '__main__':
    remove_cache()

# input()
