#10.armstrong number
n=int(input("enter a number:"))

sum=0

temp=n
while temp>0:
    digit=temp%10

    sum+=digit**3

    temp=temp//10


if n==sum:
    print(n,"is an armstrong no")
else:
    print(n,"is not an armstrong no")