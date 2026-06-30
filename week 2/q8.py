x, y, z = int(input()), int(input()), int(input())

if x == y and y == z:
    print('equilateral')
elif x == y and x != z:
    print('isosceles')
elif x == z and x != y:
    print('isosceles')
else:
    print('scalene')

x, y, z = int(input()), int(input()), int(input())

if x == y and y == z:
    print('equilateral')
elif x == y or y == z or x == z:
    print('isosceles')
else:
    print('scalene')
  
  #answer  enter number 5 5 8
  #issosceles
  