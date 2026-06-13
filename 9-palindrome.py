#palindrome checker
num=int(input("enter any number of your choice: "))
temp=num
rev=0
while temp!=0:
    rev= rev*10+temp%10
    temp=temp//10
if rev == num:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
