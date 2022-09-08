#書き込みとファイルを閉じる指示
st = open("st.txt", "w")
st.write("Hello World!!")
st.close()

#書き込み後自動でファイルを閉じる
with open("st.txt", "w") as f:
    f.write("Hello World!!!")

#読み込み
with open("st.txt", "r")as f:
    print(f.read())

#コンテナに入れて読み込む
my_list = []

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

#CSVファイルに書き出し
import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#csvファイルを読み込み
import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))