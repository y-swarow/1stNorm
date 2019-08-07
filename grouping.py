'''
第一正規化の逆変換を行うプログラム
・実行方法
python grouping.py tsvfile

 - tsvfile (optional)
   読み込むtsvファイルを指定します.
   指定しなかった場合デフォルトで './data/test_group.tsv'

・出力先
   './data/result_group.tsv'
   変更はできません

・実行例
python grouping.py
python grouping.py ./data/test_norm.tsv
'''

import sys
import os
import tsv_convert

# ファイルが存在ｓるかチェック
# 存在しなければプログラムを終了する
def filecheck(filepath):
    if not( os.path.exists(filepath) ):
        print("Error : File is not exist")
        exit()

def main():
    args = sys.argv
    if len(args) == 1:
        # ファイルが指定されていない場合 default
        filepath = './data/test_group.tsv'
        filecheck(filepath)
    elif len(args) == 2:
        # 入力されたファイルパスを受け取る
        filepath = args[1]
        filecheck(filepath)
    else:
        print("Error : argument is more than 1")
        exit()

    convert = tsv_convert.tsv_convert()
    convert.to_grouping(filepath)
    convert.output()
    convert.save('./data/result_group.tsv')

if __name__ == '__main__':
    main()
