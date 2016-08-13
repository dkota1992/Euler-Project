num = 100
while True:
    if str(num)[:2] == '17':
        num = 10**(len(str(num)))

    if sorted(str(num)) == sorted(str(num*2)):
        if sorted(str(num*3)) == sorted(str(num*4)):
            if sorted(str(num*5)) == sorted(str(num*6)):
                print(num)
                break

        num = num +1
