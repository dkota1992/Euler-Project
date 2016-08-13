import time
start = time.clock()
def fact(num):
    if num>1:
        return num*fact(num-1)
    return 1

def ncr(n,r):
    return fact(n)//(fact(r)*fact(n-r))

count = 0
for i in range(1,101):
    for j in range(1,101):
        if i<j: continue
        if ncr(i,j)>1000000: count = count+1


print(count)

stop = time.clock()

print(stop-start)
        

~ 300 ms
