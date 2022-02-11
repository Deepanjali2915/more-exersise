list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new=[]
for i in list2:
    list1.append(i) 
    for j in list1:
        if j not in new:
            new.append(j)       
print(new)          