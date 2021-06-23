songs = {"1":"fun",
         "2":"blue",
         "3":"me",
         "4":"floor",
         "5":"live"
         }

n = input("数字を入れてください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません。")

## 辞書はキーを受け取って、バリューを返すということかな。

## なかったときの例外?を見てみる
n = input("数字を入れてください:")
try:
    song=songs[n] ##KeyError
    print(song)
except(KeyError):
    print("その値はありません。")