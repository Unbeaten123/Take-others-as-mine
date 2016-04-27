# -*- coding: utf-8 -*-
#利用fliter函数输出1000范围内的所有质数
#Using the fliter function to print all the prime number within 1000
def Prime_num(n):
    if n == 2 or n == 3:
        return True
    elif n == 1 or n == 4:
        return False
    for k in range(2, n/2):
        if (n%k == 0):
            return False
    return True

for i in filter(Prime_num,range(1,1000)):
    print i
