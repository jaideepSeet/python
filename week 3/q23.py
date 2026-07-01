n=5
total=0

for i in range(1,n+1):
    total+=1/i
    a=n/total
print(total)
print(a.__round__(2))
#answer    2.283333333333
          #2.19