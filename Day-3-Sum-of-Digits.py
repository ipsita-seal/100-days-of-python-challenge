#Sum of Digits
num=int(input("enter any number of your choice: "))

temp=num
sum_digits=0
while temp!=0:
    sum_digits+=temp%10
    temp=temp//10

print(f"Sum of digits in {num} is {sum_digits}")
