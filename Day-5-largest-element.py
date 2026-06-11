#Find Largest Element in a List
#Problem Statement: Take a list of numbers from the user and find the largest element without using max().

#method 1
list_of_num=eval(input("enter a list of numbers separated by commas(,): "))
list_of_num=list(list_of_num)
print(f"list: {list_of_num}")
max_no=list_of_num[0]
for i in list_of_num:
    if i>max_no:
        max_no=i
print(f"largest element in the list: {max_no}")

#method 2
list_of_num=sorted(list_of_num)
print(f"list: {list_of_num}")
index=len(list_of_num)-1
max_num=list_of_num[index]
print(f"largest element in the list: {max_num}")
