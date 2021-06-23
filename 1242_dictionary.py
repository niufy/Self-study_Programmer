## dictionary の作成

## いっこめ
my_dict=dict()

## にこめ（なみかっこのみ）
my_dict={}

## キーとバリューの追加
fruits={"Apple":"Red",
        "Banana":"Yellow"}

## バリューの追加
fruits["Mikan"]="Orange"
## キーで参照 Orangeと表示
print(fruits["Mikan"])

## バリューの追加
fruits["Meron"]="Green"
## キーで参照 Greenと表示
print(fruits["Meron"])

## バリューの追加
fruits["Younashi"]="YellowGreen"
## キーで参照
print(fruits["Younashi"])

## in でバリューを検索←うまくいかない
b = "Red" in fruits
print(b) ## falseと出る

## not in でも検索してみる
c="Blue" not in fruits
print(c) ## Trueと出る 

## キーバリューペアの削除 delを使う
del fruits["Meron"]
print(fruits)