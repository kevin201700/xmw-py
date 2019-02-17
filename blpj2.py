print("三更半夜","厕所边上","班主任","在洗澡")
num=(13, 23,  87, 3, 136)
print("最大值是"+str(max(num)))
print("最小值是"+str(min(num)))
print('''text''')
print("可以提前"+str(12-(50*12/(50+10)))+"分钟回到学校")
num2 = (8, 7, 9, 11, 3, 5, 12, 20, 30, 18)
num3 = 0
for x in range(len(num2)):
     num3 += num2[x]
num3 -= max(num2)
num3 -= min(num2)
num3 = num3/(len(num2)-2)
print(num3)
