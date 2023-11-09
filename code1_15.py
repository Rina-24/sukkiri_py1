price = int(input("料金を入力＞＞"))
number = int(input("人数を入力＞＞"))
payment = price / number
print("お支払いは", payment , "円です")

""""
戻り値がstr型になっているのでこのままではエラーになる！
そのため入力された文字列型を数字（int型）にかえなくてはいけない
そのためint()を使う。Javaのキャストでは（int)を頭につけるけど少し違うので注意
"""