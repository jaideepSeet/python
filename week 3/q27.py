# Write a program to print the first and last digits of a number without converting it to string.

n=256

last=n%10

first=n

while first >=10:

    first=first//10

print(first,last)