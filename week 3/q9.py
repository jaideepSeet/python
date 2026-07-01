

for i in range(5,0,-1):
    fop=""
    lop=""
    for j in range(i,0,-1): 
        fop+=str(j)+" " 
        if not j==1:
         lop=" "+str(j)+lop
    print(str(fop+lop[1:]).center(5*4-1))
