import os
from posixpath import abspath

my_file=open("1890_sample_file.txt","r",encoding="utf-8")
for line in my_file:
    print(line)

##絶対パス
##abs_path=abspath("1890_sample_file.txt").replace("/",os.sep)
##print(abs_path)
##abs_file=open(abs_path)
##for line in abs_file:
##    print(line)