import math
import time
start = time.clock()
def is_prime(x):
    if x == 0 or x == 1: return False
    for r in range(2, int(math.floor(x**0.5)) +1):
        if x%r == 0: return False
    return True

def is_truncable(i):
    if len(str(i))>1 and is_prime(i):
        for k in range(len(str(i))-1):
            if not is_prime(int(str(i)[:-k-1])) or not is_prime(int(str(i)[k+1:])): return False
        return True
    else: return False

kk = set([2,3,5,7])
final = ()

while True:
    try:
        for i in kk:
            for j in range(10):
                if is_prime(int(str(i)+str(j))):
                    kk.add(int(str(i)+str(j)))
        if len(filter(is_truncable,kk)) == 11: break
    except RuntimeError: pass

print(sum(filter(is_truncable,kk)))
stop = time.clock()
print(stop-start)
