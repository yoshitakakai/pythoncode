# ファイルを読み込みモードで開く
with open('keyword01', 'r') as f:
    # ファイルの中身を読み込む
    data = f.read()

# スペースを「,」に置換する
data = data.replace(' ', ',')

# ファイルを書き込みモードで開く
with open('keywordoutput.txt', 'w') as f:
    # ファイルに書き込む
    f.write(data)