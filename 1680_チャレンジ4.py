while(True):
    str=input("数字を一桁入力してください。終了する場合はqを入力してください。：")

    seikai=["2","3","6"]
    
    if(str=="q"):
        break
    
    if(str in seikai):
        print("正解！")
    else:
        print("残念！")
