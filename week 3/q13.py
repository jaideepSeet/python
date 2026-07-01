# Write a code to accept a string as input and determine if it is a palindrome or not.

s=input("Enter the number:")
rev=""

for i in s:    #sant
    rev = i+rev #tnas
    
if s == rev:
    print("palindrome")

else:
    print("Not palindrome ")
 #Answer  enter a number 5        palindrome