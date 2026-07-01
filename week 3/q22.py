# Write a program to find the highest common factor (HCF) of two numbers.

a=10 #1 2 5 10
b=12 #1 2 3 4 6 12

hcf = 1
for i in range(min(a,b),0,-1):
    if a % i == 0 and b % i == 0:
        hcf=i
        break
print(hcf)   


        
        