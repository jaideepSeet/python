# Two numbers n1 and n2 are said to be the same if they have an equal number of digits in them. 
# Write a program to check whether n1 and n2 are the same. n1 and n2 are positive 
# integers entered by the user without converting the number 
# to string.

a=123
b=2560

count = 0
while a > 0:
    a //=10 
    count=count+1

count_b=0
while b > 0:
    b//= 10
    count_b=count_b+1

if count == count_b:
    print("same")
else:
    print("Not same")    