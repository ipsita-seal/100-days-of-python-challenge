def isprime(n):
    if n==1 or n==0:
        return "neither Prime nor composite"
    for i in range(2,n//2):
        if n%i == 0:
            return "composite"
    return "prime"

num = int(input("enter a number to check if it is prime or not: "))
print(f"{num} is ", isprime(num))
