# Write a program to accept the positive integer n from the user and print counting of numbers which are not

# prime from 1 to n.

n=int(input("Enter the number : "))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print(count)
        