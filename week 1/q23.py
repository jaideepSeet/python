# Accept a two digit number as input and print the sum of its digits.
# What about a three digit number?

# input = 256
# ouput = 2 5 6

n = int(input())
fir = n // 100
print(fir)

sec = (n // 10)%10
print(sec)

thir = n % 10
print(thir)
print(fir,sec,thir)

# print(fir+sec+thir)
#output  enter number 256
                     #2
                     #5
                     #6
                     #2 5 6































