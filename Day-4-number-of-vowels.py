#count number of vowels
string=input("enter a string: ")
vowels=['A','E','I','O','U']
string=string.upper()
count=0
for i in string:
    if i in vowels:
        count+=1
print(f"there are {count} number of vowels")
