"""找出所有的水仙花数"""
for num in range(100,1000):
    low = num % 10 #计算出个位数
    mid = num // 10 % 10#计算出十位数
    high = num // 100 #计算出百位数
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
