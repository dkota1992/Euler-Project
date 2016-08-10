import math
import time
start = time.clock()
def Divisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    divList.remove(x)
    return divList

n = 10000
B = [False]+[True]*(n-2)
num = 1
kk = []

while num<n-1:
    if B[num]:
        x,y = sum(Divisors(num)),sum(Divisors(sum(Divisors(num))))
        if y == num and x!=y:
            kk.append(num)
            B[y] = False
        elif x<n:
            B[x] = False

    num = num+1

print(kk,time.clock()-start)
