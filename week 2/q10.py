# Accept three integers as input from the user. Print good triplet if one of the three numbers is the sum of the other two, and bad triplet otherwise.


# x,y,z=map(int,(input("Enter the number:")).split())

# if x+y==z or y+z==x or z+x==y:
#     print("good tub")
# else:
#     print("bad")


x = int(input("Enter an integer: "))

last_digit = abs(x) % 10

digits = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]

print(digits[last_digit])



#answer enter an integer 147
#answer Seven