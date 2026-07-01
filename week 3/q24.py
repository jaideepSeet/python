# Write a program to print the Fibonacci series of n terms where n is always greater than or equal to 2.

n=int(input())
a=0
b=1
print(a)
print(b)

for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
    