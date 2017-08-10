# coding utf-8
import pprint
import requests


def main():
    # GETパラメータはparams引数に辞書で指定する

    response = requests.get(
        'http://127.0.0.1:5000/get',
        params={'foo': 'bar'})
    # レスポンスオブジェクトのjsonメソッドを使うと、
    # JSONデータをPythonの辞書オブジェクトを変換して取得できる。
    pprint.pprint(response.json())


if __name__ == '__main__':
    main()
input()
