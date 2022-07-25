songs = {"1": "fun",
         "2": "blue",
         "3": "me"
         }

n = input("数字を入力してください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません")