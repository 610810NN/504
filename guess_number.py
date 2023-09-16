"""
随机产生一个1到10的数字，你有三次机会去尝试。
"""
import random
num = random.randint(1,10)
print("你有三次机会猜数字")
numbe=int(input("第一次机会，请输入一个数字"))
if numbe==num :
    print("恭喜你，一次猜对")
elif numbe>num:
    print("你的数字偏大，第二次机会，再输入一个数字")
    numbe2=int(input())
    if numbe2==num:
        print("第二次机会猜对")
    elif numbe2>num:
        print("你的数字偏大，最后一次机会，再输入一个数字")
        numbe3=int(input())
        if numbe3==num:
            print("最后一次机会，终于猜对啦")
        else :
            print("猜错了，没机会啦")
    elif numbe2<num:
        print("你的数字偏小，最后一次机会，再输入一个数字")
        numbe3 = int(input())
        if numbe3 == num:
            print("最后一次机会猜对")
        else:
                print("猜错了，没机会啦")
elif numbe<num:
    print("你的数字偏小,第二次机会，再输入一个数字")
    numbe2 = int(input())
    if numbe2 == num:
        print("第二次机会猜对")
    elif numbe2 > num:
        print("你的数字偏大，最后一次机会，再输入一个数字")
        numbe3 = int(input())
        if numbe3 == num:
            print("最后一次机会，终于猜对啦")
        else:
            print("猜错了，没机会啦")
    elif numbe2 < num:
        print("你的数字偏小，最后一次机会，再输入一个数字")
        numbe3 = int(input())
        if numbe3 == num:
            print("最后一次机会猜对")

        else:
            print("猜错了，没机会啦")
print(f"最初的数字是{num}")