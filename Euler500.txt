from time import time
import math
start = time()


num = 10000000

def prime_primesquares(num):
    A = [False]*2+ [True]*num
    k = math.sqrt(num)
    for i,j in enumerate(A):
        if j:
            yield i
            for n in range(i*i, num, i): 
                A[n] = False
                
            if i<k: A[i**2] = True
result = 1                   
j = 1
k = 1
g = prime_primesquares(num)
while j<500500+ 1:    
    k = g.next()
    j = j+1
    result = result*k%500500507

print(j,result,time()-start)

