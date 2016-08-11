import math
import time
start = time.clock()

def prime_onlyodd(num):
    A = [False]*2 + [True]*(num-2)
    yield 2
    for i, j in enumerate(A):
        if j:
            if any([int(c)%2 == 0 for c in str(i)]): pass
            else : yield i
            for k in range(i*i,num-1,i):
                    A[k] = False

def is_prime(num):
    base, i = math.sqrt(num)+1,2
    while i<base:
        if num%i == 0:
            return False
        i = i+1
    return True
    
def is_circular(num):
    n,num = 1,str(num)
    while n<len(num):
        if not is_prime(int(num[-n:]+num[:-n])):return False
        n = n+1
    return True

pr_onl = prime_onlyodd(2000000)
pr_on_pr = pr_onl.next()
count = 0
while pr_on_pr<100:
    if is_circular(pr_on_pr): count = count +1
    pr_on_pr = pr_onl.next()

print(count,time.clock()-start)


                
            
            
