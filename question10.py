b = [[45, 21, 42, 63], [12, 32, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# i = 0
# while i < len(big_list):
#     small_list_length = len(big_list[i])
#     j = 0
#     while j < small_list_length:
#         print (big_list[i][j])
#         j=j+1
#     i = i+1
#     print ('-----')
    # print(small_list_length)

# i=0
# while i<len(big_list):
#     small=len(big_list[i])
#     j=0
#     max=0
#     while j<small:
#         if big_list[i][j]>max:
#             big_list[i][j]=max
#             print(max)  
#         j+=1
#     i+=1   




# i=0
# while i<len(big_list):
#     j=0
#     max=big_list[i][0]
#     max2=big_list[i][0]
#     while j<len(big_list[i]):
#         if big_list[i][j]>max:
#             max=big_list[i][j]
#         j+=1
#     # i+=1
#     print(max,"1")
#     # print(max2,"2")
#     i+=1    


# i=0
# while i<len(b):
#     max=0
#     j=0
#     while j<len(b[i]):
#         if b[i][j]>max:
#             max=b[i][j]
#         j=j+1
#     # i=i+1
#     # print(max)
#     max1=0
#     j=0
#     while j<len(b[i]):
#         if b[i][j]>max1:
#             if b[i][j]!=max:
#                 max1=b[i][j]
#         j=j+1
#     i=i+1
#     print(max1)


# i=0
# while i<len(b):
#     max=0
#     j=0
#     while j<len(b[i]):
#         if b[i][j]>max:
#             max=b[i][j]
#         j=j+1
#     # print(max)
#     max1=0
#     k=0
#     while k<len(b[i]):
#         if b[i][k]>max1:
#             if b[i][k]!=max:
#                 max1=b[i][k]
#         k=k+1
#     i=i+1
#     print(max1)




a= {1: 'NAVGURUKUL',2: 'IN',3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
for i in a:
    for z in a[i]:
        del(a[3]['A'])
        print(a)
