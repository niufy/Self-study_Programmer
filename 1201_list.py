colors={"green","red","blue"}

guess=input("何色でしょう？（入力してください）：")

if guess in colors:
    print("正解！")
else :
    print("残念！")