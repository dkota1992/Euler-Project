def leapyear(year):
    if year%400 == 0: return True
    elif year%100 == 0: return False
    elif year%4 == 0: return True
    else: return False

year_1901 = [1,4,4,0,2,5,0,3,6,1,4,6]

year = 1902
count = 2

while year<=2000:
    if leapyear(year):
        for i in range(len(year_1901)):
            if i>1: year_1901[i] = year_1901[i]+2
            else: year_1901[i] = year_1901[i] + 1
    elif leapyear(year-1):
        for i in range(len(year_1901)):
            if i>1: year_1901[i] = year_1901[i]+ 1
            else: year_1901[i] = year_1901[i] + 2
    else:
        for i in range(len(year_1901)):
             year_1901[i] = year_1901[i]+ 1
    year = year + 1

    for i in year_1901:
        if i%7 == 1: count = count + 1


print year_1901,count
