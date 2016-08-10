def prod(x,y):
    return x*y
B = [False]*2 + [True]*1000
for i, prime in enumerate(B):
    if prime:
        for k in range(2*i,1000,i):
            B[k] = False
BB = [i for i,prime in enumerate(B) if prime]
pres_num = 1
num = 1
while True:
    num = num + 1
    pres_num = pres_num + num
    aj = pres_num
    k = [0]
    j = 0
    for i in BB:
        if aj == 1: break
        if aj%i == 0:
            k.append(0)
            j = j+1
        while aj%i == 0:
            aj = aj/i
            k[j] = k[j] +1
    if reduce(prod,map(lambda x:x+1,k))>500: break

print(pres_num)
