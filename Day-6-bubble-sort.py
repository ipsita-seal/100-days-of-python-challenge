#Bubble sort
l1=[9,8,7,6,5,4,3,2,1,0]
for i in range(1,len(l1)):
    for i in range(len(l1)-1):
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1)
