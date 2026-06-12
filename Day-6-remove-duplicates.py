#remove duplicates from list without set
size=int(input("enter size of list: "))
l1=[]
for i in range (size):
    element=int(input(f"Enter Element{i}: "))
    l1.append(element)
print(f"original list: {l1}")
unique=[]
for i in l1:
    if i not in unique:
        unique.append(i)
print("list after removing duplicates without set(): ", unique)

#remove duplicates from list with set
size=int(input("enter size of list: "))
l1=[]
for i in range (size):
    element=int(input(f"Enter Element{i}: "))
    l1.append(element)
print(f"original list: {l1}")
print("list after removing duplicates with set(): ", list(set(l1)))
