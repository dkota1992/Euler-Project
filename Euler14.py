import time
start = time.clock()
n = 1000000
result= 0
comp = 0
kk = [True]*(n+3)
it = 0
while n>100:
    if kk[n]:
        count = 0
        num = n
        it = it + 1
        while num != 1:
            if num%2 == 0: num = num/2
            else: num = 3*num+1
            if num<n:
                if kk[num]: kk[num] = False
            count = count +1
            if count>comp:
                result = n
                comp = count
    n = n-1


print(result,comp,it,time.clock()-start)
