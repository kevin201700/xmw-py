print()#输出 打印 显示
input()#输入
int()#字符串转数字
str()#数字转字符串
max(1, 2)#取最大值
min(1, 2)#取最小值
while True:#无限循环-Ctrl-c停止
    break

import random
print(random.randint(1, 6))
print(random.randint(1, 10))
no = random.randint(1, 3)
if no == 1:
    print("李")
elif no == 2:
    print("铭")
elif no == 3:
    print("昊")

name = input("请问您叫什么名字：")
print("你好，" + name)