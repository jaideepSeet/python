# Accept a positive integer as input and print True if it is a perfect 
# square and False otherwise. For example, if the input is 25 ,
# then you must print True . If the input is 15 , then you must print False


n=int(input()) #81
root=int(n**0.5) #81*0.5*0.5 = 9
print(root*root==n) #81==81

#4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961
#output 81   True
