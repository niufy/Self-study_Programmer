lists=[]

rap=["カニエ・ウエスト","ジェイ・ｚ","エミネム","ナズ"]
rock=["ボブ・ディラン","ザ・ビートルズ","レッド・ツェッペリン"]
djs=["ゼッズ・デッド","ティエスト"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap=lists[0] ##　たぶんこれは参照型。
## なので、rapに追加すると、list[0]も更新される

rap.append("ケンドリック・ラマ―")
print(rap)
print(lists)