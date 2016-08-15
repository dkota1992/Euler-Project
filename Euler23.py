import math
import time
start = time.clock()
def Divisors(x):
    if x == 0: return [1]
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    divList.remove(x)
    return set(divList)

def nonabun(x):
    return sum(Divisors(x)) <= x

num = 28123
A = [False] + [True]*num
n = 1
B = [x for x,cond in enumerate(A) if not nonabun(x)]
B.remove(0)

A = [False] + [False]*num
for i in B:
    for j in B:
        if i+j<num+1:
            A[i+j] = True
        else: break

K = [i for i,j in enumerate(A) if not j]
print(sum(K),time.clock()-start)
