n=int(input("Enter the number : "))
op=0

for i in range(1,n+1):
    op+=int(i*'1')
    avg=op/n
print(op)
print(avg)
