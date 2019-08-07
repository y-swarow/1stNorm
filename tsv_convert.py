# パッケージの読み込み
import csv
import itertools

# セルの中の値の最大数
CELL_MAX_VALUE = 10

class tsv_convert:

    def __init__(self):
        # 読み込んだデータ用
        self.data = []
        # 出力するデータ用
        self.result = []

    # tsv ファイルを読み込み
    def read_tsv(self, filename):
        # 初期化
        self.data = []
        # tsvファイルの読み込み
        with open(filename, "r") as tsvfile:
            tsv = csv.reader(tsvfile, delimiter = '\t')
            # １行目だけを読み込み（ヘッダーがある場合）
            # header = next(tsv)
            # データの読み込み
            for line in tsv:
                self.data.append(line)

    def output(self):
        print("--- converted result (list)----")
        for data in self.result:
            print(data)

    def get(self):
        return self.result

    # tsv形式で ファイルに保存
    def save(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            for data in self.result:
                writer.writerow(data)

    # 第一正規形に変換
    def to_norm1st(self, filename):
        # 初期化
        self.result = []
        # tsv ファイルを読み込み
        self.read_tsv(filename)

        # １行ずつ読み込んで処理していく
        for line in self.data:
            # セミコロンで区切ってリスト化したものを、セルごと保存
            cells_splited = []
            # セルを1つ取り出して、セミコロンで区切ってリスト化する
            for cell in line:
                cell_splited = cell.split(";")
                cells_splited.append( cell_splited )

            # 第一正規化を行う
            values =  list(itertools.product(*cells_splited))
            # 結果を保存
            for value in values:
                    self.result.append( list(value) )

    # グループ化する
    def to_grouping(self, filename):
        # tsv ファイルを読み込み
        self.read_tsv(filename)
        # 読み込んだファイルを昇順に並び替える(1行目を基準)
        self.data.sort()

        # グルーピングを行う
        # 初期化
        key = self.data[0][0]   # 1行1列目
        value_count = 1         # セル中の値の数を管理
        # 1行目を取得
        self.result = [self.data[0]]
        # 2行目以降をグループ化
        for data in self.data[1:]:
            # key が同じときセミコロンで連結
            if (data[0] == key and value_count < CELL_MAX_VALUE ):
                self.result[-1][1] = self.result[-1][1] + ";" + data[1]
                value_count += 1
            elif ( data[0] == key ):
                self.result.append(data)
                value_count = 1
            # key と異なる場合、次のグループへ
            else:
                self.result.append(data)
                key = data[0]
                value_count = 1
