"""
Binary to Number Converter
Problem Statement: Convert a binary number to decimal manually
"""

def bin_to_dec(bin_n):
    num,power=0,0
    while bin_n>0:
        temp=bin_n%10
        num=num+ temp*(2**power)
        power+=1
        bin_n//=10
    return num
    
binary_num=int(input("enter a binary number: "))
print(f"Decimal of {binary_num} is {bin_to_dec(binary_num)}")
