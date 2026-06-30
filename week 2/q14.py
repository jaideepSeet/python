# The following string is encoded using the Caesar cipher with a shift of 5: udymts . Decode the string!


encoded = "udymts"
shift = 5
decoded = ""

for char in encoded:
    new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    decoded += new_char

print(decoded)
#answer python