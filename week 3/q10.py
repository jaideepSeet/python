# Write a code to accept the string of length 10 from the user and print
# True if string has any character

# occurring 5 times consecutively in it, otherwise print False.

s="hellooooghu"
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in alpha:
    # print(i)

    if i*5 in s:
        print("true")
        break
else:
    print("false")
        
         
