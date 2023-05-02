# ファイルを読み込みモードで開く
with open('keyword.txt', 'r') as f:
    # ファイルの中身を読み込む
    data = f.read()
    # 全角スペースを半角スペースに置換する
    data = data.replace('　', ' ')
    # スペースを「,」に置換する
    data = data.replace(' ', ',')

# ファイルを書き込みモードで開く
with open('keywordoutput.txt', 'w') as f:
    # ファイルに書き込む
    f.write(data)

#番号振り分け
with open('keywordoutput.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # 行数の初期化
    line_number = 1

    # 1行ずつファイルを読み込み、行頭に番号をつけて出力
    for line in input_file:
        output_file.write(f"{line_number}.{line}")
        line_number += 1

