# 次の各式が評価されていく過程と結果を表記する。途中でエラーが発生するものは、その箇所でエラーと表記する。

# (1) 2 + 10 * 5 ⇒ 2 + 50 ⇒ 52

# (2) "7" * (3 + 4) ⇒ "7777777"

# (3) "version{}".format(3 + 2 * 0.1 + 9 * 0.01) ⇒ "version{}".format(3 + 0.2 + 9 * 0.01)
#                                                ⇒ "version{}".format(3 + 0.2 + 0.09)
#                                                ⇒ "version{}".format(3.2 + 0.09)
#                                                ⇒ "version{}".format(3.29)
#                                                ⇒ "version3.29"

# (4) 4 * "num" + "回目のTypeError" ⇒ "numnumnumnum" + "回目のTypeError"
#                                   ⇒ "numnumnumnum回目のTypeError"