tv = ["GOD", "Narcos", "Vice"]
i = 0
for show in tv:
#showをtvに取り込む
    new = tv[i]
#tv[i]をnewに変換
    new = new.upper()
#newに変換したtv[i]を大文字化
    tv[i] = new
#大文字化されたtv[i]をtv[i]に変換し直す
    i += 1
#tvの値の位置をひとつずらす

print(tv)
#全てを繰り返したあと、tvを出力