bitcoins = int(input())
chinese_yuans = float(input())
commision = float(input()) /100

bitcoins_to_leva = bitcoins * 1168
chinese_yuans_to_dollars = chinese_yuans * 0.15
dollars_to_leva = chinese_yuans_to_dollars * 1.76

leva = bitcoins_to_leva + dollars_to_leva
euro = leva / 1.95

euro -= euro * commision
print("%.2f" % euro)

