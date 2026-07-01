# Write a code to accept a string as input and reverse it using loop:

s="hello"
op=""

for i in range(len(s)-1,-1,-1): 
    op+=s[i]
print(op)    

#Answer    olleh