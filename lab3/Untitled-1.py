string = "s`mh`"
new_string = ""
a = int(input())
for char in string:
    new_string += chr(ord(char) + a)

print(new_string)