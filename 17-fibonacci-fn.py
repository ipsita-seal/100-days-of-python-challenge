"""
Fibonacci Using Functions
Problem Statement: Create a function that generates Fibonacci numbers up to N terms.
n=8 | series: 0,1,1,2,3,5,8,13
"""
#iterative method
def Fibonacci_series(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        c=a+b
        a=b
        b=c
    return
    
num = int(input("enter limit: "))
print("Fibonacci series upto {num} terms:")
Fibonacci_series(num)

#recursive method
def fibo(n):
    if n==0: return 0
    if n==1: return 1
    return fibo(n-1)+fibo(n-2)

n=int(input("\n\nenter a limit: "))
for i in range (n):
    print(fibo(i), end=" ")
