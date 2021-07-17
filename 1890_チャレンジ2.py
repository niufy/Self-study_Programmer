result=input("好きな色は何ですか？：")
text_file="1890_color.txt"
with open(text_file,"w",encoding="UTF-8") as f:
    f.write(result)
print("書き込みました。")