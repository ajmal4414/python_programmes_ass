#4.string is palindrome or not
str=(input("enter a string:"))

l=len(str)
rev_str=str[l::-1]

if str==rev_str:
    print("string is palindrome")
else:
    print("string is not palindrome")