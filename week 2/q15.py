# A three digit number is called a 
# sandwich number if the difference 
# between its first and last digit is
#  equal to its middle digit. Accept 
# a three digit number as input and 
# print sandwich if the number is a 
# sandwich number. Print plain if the
#  number is not a sandwich number. For
#  example, 123 and 853 are sandwich
#  numbers.

n=int(input())
first_digit = n // 100
middle_digit = (n // 10) % 10
last_digit = n % 10
if abs(first_digit - last_digit) == middle_digit:
    print("sandwich")
else :
        print("plain")
