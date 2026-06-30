# Accept three non-negative real numbers as input from the user. If the three numbers form the sides of a triangle, print True . If not, print False.
# Accept three non-negative real numbers from the user
a, b, c = map(float, input("Enter three numbers: ").split())

# Check the triangle inequality condition
if a + b > c and a + c > b and b + c > a:
    print(True)
else:
    print(False)
#answer enter three number 5 2 1
#false