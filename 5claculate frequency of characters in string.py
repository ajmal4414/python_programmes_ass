# 5.write code calculate frequency of characters in a string
str=("hello world")
dict={}


for i in str:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] =1

print(dict)
