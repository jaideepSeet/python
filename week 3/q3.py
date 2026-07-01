# Write a program to accept the positive integer n from the user and print the average of all number's factorial

# from 1 to n .
n=int(input("ENter the number :"))

fact = 1

total = 0
 
avg = 0

for i in range (1,n+1):#12345
    fact=fact*i # 1*1=1 1*2=2 2*3=6 6*4=24 24*5=120
    total=total+fact # 0+1=1 1+2=3 3+6=9 9+24=33 33+120=153
    avg=total/i # 1/1=1 3/2=1.5 9/3=3 33/4=8.25 153/5=30.6
    
print(fact)
print(total)
print(avg)