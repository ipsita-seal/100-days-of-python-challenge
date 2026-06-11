#Find Second Largest Element
#Problem Statement:Find the second largest element in a list.

list_of_num=eval(input("enter a list of numbers separated by commas(,): "))
print(f"list: {list(list_of_num)}")
list_of_num=list(sorted(set(list(list_of_num))))
index=len(list_of_num)-2 #to get 2nd largest element
max_num=list_of_num[index]
print(f"2nd largest element in the list: {max_num}")
