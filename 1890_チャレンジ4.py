import csv
from os import write
movies=[["トップガン","リスキービジネス","マイノリティリポート"],
        ["タイタニック","ザレブナント","インセプション"],
        ["トレーニングデイ","マンオンファイア","フライト"]]

with open("1890_movies2.csv","w",encoding="utf-8") as f:
    for str in movies:
        csv_str=",".join(str)
        f.write(csv_str)