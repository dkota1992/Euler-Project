def palindromic(num):
    return str(num) == str(num)[::-1]

num = 1
count = 0
while num<10000:
    pres = num
    for i in range(1,50):
        if palindromic(pres) and num != pres:
            count = count +1
            break
        else: pres = int(str(pres))+int(str(pres)[::-1])

    num = num + 1

print(9999-count)
