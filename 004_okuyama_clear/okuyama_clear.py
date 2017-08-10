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
from logging import basicConfig, getLogger, DEBUG

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
    # ロギング件数の間隔
    border = 1000

    # キーの生成ルール
    pre = ''
    sitecode = ''

    # 対象ファイルの抽出
    gz_list = glob.glob('./*.gz')
    z_list = glob.glob('./*.zip')

    logger.debug('# 実行時のパス : ' + os.path.abspath(__file__))

    # ---------------
    # gzファイル群
    # ---------------

    for gz_file in gz_list:

        logger.debug('## 対象のgzファイル名 : ' + gz_file)

        name, ext = os.path.splitext(gz_file)
        # ファイル名のルールからキャッシュキー生成用の値を取得
        pre , sitecode = getPrefix(name)

        w = open(name + '.log', 'wb')

        if os.path.isfile(gz_file) == False:
            logger.debug('isfile : ' + gz_file + ' is not found')
            continue

        # これから作業する行数の事前表示
        num_lines = sum(1 for line in gzip.open(gz_file))
        logger.debug('### ファイル内の行数 : ' + str(num_lines))

        with gzip.open(gz_file, 'rt', "utf_8") as lines:

            for (index, line) in enumerate(lines):
                key = line.rstrip(newline)
                if key != '' :

                    key = getCacheKey(pre, sitecode, key)

                    # ここでキーを投げる

                    # php のOkuyamaClassをnewしたうえで
                    # removeValue($key)を行うAPIをキックする

                    w.write(line.encode('utf-8'))
                    break

                if index % border == 0: logger.debug('#### ' + str(index) + '件を通過')

                # リクエスト周期
                sleep(second)

        w.close()

    # ---------------
    # zipファイル群
    # ---------------

    for z_file in z_list:

        logger.debug('## 対象のzipファイル名 : ' + z_file)

        with zipfile.ZipFile(z_file, 'r') as file_list:

            file_list.extractall()

            for file_name in file_list.namelist():

                if fnmatch.fnmatch(file_name, '*.txt'):

                    # ファイル名のルールからキャッシュキー生成用の値を取得
                    pre , sitecode = getPrefix(file_name)

                    w = open(file_name + '.log', 'wb')
                    # pprint.pprint(file_name.rstrip(newline))

                    if os.path.isfile(file_name) == False:
                        logger.debug('isfile : ' + file_name + ' is not found')
                        continue

                    logger.debug('### 対象のファイル名 : ' + file_name)

                    # 全行数
                    num_lines = sum(1 for line in open(file_name))
                    logger.debug('#### ファイル内の行数 : ' + str(num_lines))

                    with open(file_name) as lines:

                        for (index, line) in enumerate(lines):
                            key = line.rstrip(newline)
                            if key != '' :
                                # 対象文字列
                                key = getCacheKey(pre, sitecode, key)

                                # ここでキーを投げる

                                w.write(line.encode('utf-8'))
                                break

                            if index % border == 0: logger.debug('##### ' + str(index) + '件を通過')

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

if __name__ == '__main__':

    basicConfig(level=DEBUG,
    filename="application.log",
    format="%(asctime)s %(levelname)-7s %(message)s")

    logger = getLogger(__name__)

    logger.debug('----------------------')
    logger.debug(os.path.basename(__file__) + 'の実行を開始')
    remove_cache()
    logger.debug(os.path.basename(__file__) + 'の実行を終了')
    logger.debug('----------------------')
