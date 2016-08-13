def fibby(): 
  a,b,c = 1,1,1 
  yield [1,a] 
  yield [2,b] 
  while True: 
    a,b,c = b,a+b,c+1 
    yield [c+1,b] 
  
kk = fibby() 
while True: 
  if len(str(next(kk)[1]))== 1000: 
    print next(kk)[0]-1 break
