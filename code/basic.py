#コメント
#これはコメントです

#出力
print("Hello, World!!")

#str
"Hello, World!!"

#int
2.2 + 3.2

#bool
True
False

#NoneType
None

#定数(絶対に変わらない値)
2 + 2
>>> 4

4 / 2
>>> 2

2 * 2
>>> 4

#変数(変わる可能性のある値)
int a=;
a = 144;

b = 100

x = 100
x
>>> 100

#タプル
coms = ("A. Development", "Friends", "Always Sunny")

#リスト
shows = ["GOT", "Narcos", "Vice"]

#辞書
#キーでバリューを検索して出力
people = {"g. Bluth IT": "A. Development",
          "Barny": "HIMYM",
          "Dennis": "Always Sunny",
          }

print(peple["Barny"])

#イテラブル　繰返し可能
#ミュータブル　変更可能
#イミュータブル　変更不可能

#文字列 大文字変換
.upper()

#文字列 小文字変換
.lower()

#文字列 最初の文字だけ大文字変換
.capitalize()

#書式化
"{}が{}で{}をした。".format("", "", "")

#分割
"xxx,yyyy".split(",")

#結合
text = "abc"
n = "+".join(text)

#文字列の最初と最後の空白を取り除く
.strip()

#置き換え xからyへ置き換え
.replace("x", "y")

#例外処理
words = ["The", "xxxxx", "Entertainment"]
one = " ".join(words)
try:
    print(one.index("mi"))
except ValueError:
    print("見つかりません")

#包含している
print("The" in one)
#包含していない
print("The" not in one)

#エスケープ文字
print("彼女は\"そうだね\"と言った")
彼女は"そうだね"と言った

#改行
print("彼女は\nそうだね\nと言った")
彼女は
そうだね
と言った

#スライス
#全出力
fruits[:]
#先頭から
fruits[:3]
#一番後ろまで
fruits[2:]
#途中スライス
fruits[1:3]

#showがshowsに含まれていたら
if show in shows:

#showをshowsの中に渡す
for show in shows

