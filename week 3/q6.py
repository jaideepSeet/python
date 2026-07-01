# Write a program to accept the two positive integers start and stop where 
# 0< start<stop<=100 print all

# numbers from start to stop both inclusive with following constraints.

# If the number is divisible by 3 print Divisible by 3 at the place of number.

# If the number is divisible by 5 print Divisible by 5 at the place of number.

# If the number is divisible by 10 print Divisible by 10 at the place of number.

# If the number is divisible by any of two from 3 ,5 and 10 , print nothing, just skip.

# If the number is divisible by all ( 3 , 5 and 10) , stop printing the number.

# If the number is not divisible by any of ( 3 , 5 and 10) , just print the number as it is.

for i in range(5,51):

    if i % 3==0 and i % 5==0 and i % 10==0:
        break
    elif i % 3==0 and i%5==0:
        continue
    elif i % 3 ==0 and i% 10==0:
        continue
    elif i%5==0 and i%10==0:
        continue
    elif i%3==0:
        print("Divisible by 3")
    elif i%5==0:
        print("Divisible by 5")
    elif i%10==0:
        print("Divisible by 10")
    else:
        print(i)
    

