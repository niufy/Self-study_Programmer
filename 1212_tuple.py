tuple_test=("a",1,"ssss")

print(tuple_test[0])
print(tuple_test[1])

## 下は例外TypeErrorが発生
## tupleは変更、追加などができない
## tuple_test[0]="a_3"

## 要素が含まれているかは in を使う
if "a" in tuple_test:
    print("aは含まれています。")
