import math
import time
start = time.clock()

def primes(num):
    A = [False]*2 + [True]*(num-1)
    for i,j in enumerate(A):
        if j:
            yield i
            for k in range(i*i,num,i):
                A[k] = False

def composite(num):
    A = [False]*2 + [True]*(num-1)
    p = primes(num)
    p_prime = p.next()
    for i in range(4,num,2):
        A[i] = False
    for i,j in enumerate(A):
        if j and i == p_prime: p_prime = p.next()
        elif j : yield i
    
def is_prime(num):
    n = math.sqrt(num)
    i = 2
    while i<n:
        if num%i == 0: return False
        i = i+1
    return True
jj = 0   
c = composite(10000)
prime_num,comp_num = [],[]
KK = True
while KK:
    n = 2
    i = 0
    com = c.next()
    while True:
        try:   
            i = i+1
            pres_prime = com - i*n
            if not is_prime(pres_prime): continue
            if i == 1: break
            elif math.sqrt((i)).is_integer():
                break
        except ValueError:
            KK = False
            print(com, pres_prime,i)
            break
        
print(time.clock()-start)

        
            






        
        
        
