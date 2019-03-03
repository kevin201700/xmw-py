import random, math
print("-------------------------------口算大师-------------------------------")
while True:
    计算_四则运算 = random.randint(1, 4)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if 计算_四则运算 == 1:
        c = a + b
        input_no = input(str(a) + " + " + (str(b) + " = "))
    elif 计算_四则运算 == 2:
        c = a - b
        input_no = input(str(a) + " - " + (str(b) + " = "))
    elif 计算_四则运算 == 3:
        c = a * b
        input_no = input(str(a) + " × " + (str(b) + " = "))
    elif 计算_四则运算 == 4:
        if a % b != 0:
            c = str(math.floor(a / b)) + " `````` " + str(a % b)
        else:
            c = str(a / b)
        input_no = input(str(a) + " ÷ " + (str(b) + " = "))

    #print(c)
    #print(input_no)
    if 计算_四则运算 == 4:
        if c == input_no:
            print("恭喜你，答对了！")
        else:
            print("答错了，加油哦！")

    else:
        if str(c) == input_no:
            print("恭喜你，答对了！")
        else:
            print("答错了，加油哦！")