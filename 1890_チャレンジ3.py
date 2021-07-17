import csv

movies=[["Top Gun","Riscky Business","Minority Report"],
        ["Titanic","The Revenant","Inception"],
        ["Training Day","Man on Fire","Flight"]]
with open("1890_movies1.csv","w",encoding="UTF-8") as f:
    for str in movies:
        csv_str=",".join(str)
        f.writelines(csv_str) 

##原案
with open("1890_movies1.csv","w") as csvfile:
    str = csv.writer(csvfile,delimiter=",")##csvのカンマを付与
    for movie_list in movies:
        str.writerow(movie_list)##カンマ付を上書き