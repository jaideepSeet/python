# Write a program to accept the positive integer n from the user and print the cube of all
# numbers from 1 to n.

 n=int(input("Enter the number : "))

 for i in range(1, n+1):
     cube = i**3
     print(f"Current number is :{i} and the cube is {cube}")