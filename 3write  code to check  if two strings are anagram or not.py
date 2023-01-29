#3.write a code to check if two strings are anagram or not
str1="race"
str2="acer"

str1=sorted(str1.lower())
str2=sorted(str2.lower())

print("str1 after sorting",str1)
print("str2 after sorting",str2)

if str1==str2:
    print("strings are anagram")
else:
    print("string are not anagram")