pp = 600851475143 
kk = 0 
mat = [] 
while True: 
  kk = kk+1 
  if pp%kk == 0: 
    mat.append(kk) 
    pp = pp//kk 
  if kk>pp: break 
    
print(max(mat))
