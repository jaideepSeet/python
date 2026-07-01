target=85
for i in range(5):
    guess=int(input())
    d=target-guess
    
    if d==0:
        print("Excelent")
    elif abs(d)<=10:
        print("good")
    elif d > 10:
        print(" Low ")   
    else:
        print("high")     