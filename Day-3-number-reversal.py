#reverse a number without converting it into a string
num=int(input("enter any number of your choice: "))
temp=num
rev=0
while temp!=0:
    rev= rev*10+temp%10
    temp=temp//10
print(f"reverse of {num} is {rev}")
