message = ("请输入一个数字，然后我会告诉你这个数是不是10的整数倍")
message += ("\n请输入：")

number = input(message)
number = int(number)

if number % 10 ==0:
    print(str(number) + "是10的整数倍")
else:
    print(str(number) + "不是10的整数倍")