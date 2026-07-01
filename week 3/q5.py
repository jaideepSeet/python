# Write a program to accept the string s from the user and print all alphabets in one line separated by , before

# first occurrence of vowels .

#s="program"
#vowel="aeiouAEIOU"
#res=""

#for i in s:
#   if i in vowel:
#        continue
#    else:
#        res+=i+","
#print(res)
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
seen_vowels = ""
res = []

for char in s:
    if char in vowels and char not in seen_vowels:
        seen_vowels += char
        res.append(char)
print(",".join(res))

