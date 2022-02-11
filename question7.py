list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
# new=[]
# i=0
# while i<len(list1):
# #     # print(i)
# #     j=0
# #     while j<len(list2):
# #         print(j)    
# #         j+=1
# #     # i+=1    
# for i in list1:
#     for j in list2:
#         if i==j:
#             new.append(i)
#         else:
#             print("sdfgh")    
# print(new)      

new=[]
for i in list1:
    if i  in list2:
        new.append(i)
print(new)        
