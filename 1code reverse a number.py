#1reversed a number
# n=123456789
# print(str(n)[::-1])

num=1234
reversed_num=0

while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("reversed",reversed_num)