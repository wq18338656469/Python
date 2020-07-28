"""使用input()函数获取键盘输入（字符串）
    使用int()函数将输入的字符串转换成整数
    使用print（）函数输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))
# c = input()
# %% 表示百分号
print('%d + %d = %d' % (a, b, a + b)) #例如6 + 3 = 9
print('%d - %d = %d' % (a, b, a - b)) #例如6 - 3 = 3
print('%d * %d = %d' % (a, b, a * b)) #例如6 * 3 = 18
print('%d / %d = %f' % (a, b, a / b)) #例如6 / 3 = 2.000000
print('%d // %d = %d' % (a, b, a // b)) #例如6 // 3 = 2
print('%d %% %d = %d' % (a, b, a % b)) #例如6 % 3 = 0(%表示求余)
print('%d ** %d = %d' % (a, b, a ** b)) #例如6 ** 3 = 216(**表示多少次方)