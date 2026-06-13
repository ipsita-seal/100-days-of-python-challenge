"""
Number to Binary Converter
Problem Statement: Convert a decimal number to binary without using bin().
"""

number=int(input("enter number: "))

def dec_to_bin(n):
    if n==0: return "0"
    bin_string=""
    while n>0:
        remainder=n%2
        bin_string = str(remainder) + bin_string
        n = n // 2
    return bin_string

print(f"Binary of {number} is {dec_to_bin(number)}")
