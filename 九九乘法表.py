"""本程序输出九九乘法表"""
for x in range(1, 10):
    for y in range(1, x+1):
        print('%d*%d=%d' % (x, y, x * y), end='  ') # %d表示占位符
    print(' ')