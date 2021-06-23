eights=["Edgar Allan Poe","Charles Dickens"]
nines=["Hemingway","Fitzgerald","Orwell"]

authors=(eights,nines)
## tupleの要素にリストなどのイミュータブルな要素を持たせた場合、イミュータブルではなくなるため、辞書のキーとして使えなくなる。
print(authors)