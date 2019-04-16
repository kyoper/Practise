# def selectionSort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 temp=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
#
#     return arr
#
# print(selectionSort([3,5,6,9,4,8]))

# for i in range(23,2):
#     print("hello")

# def sum(arr):
#     if len(arr)==0:
#         return 0
#     return arr.pop(0)+sum(arr)
#
# print(sum([2,3,5,6]))


# def listLength(list):
#     if len(list)==1:
#         return 1
#     list.pop()
#     return 1+listLength(list)
#
# print(listLength([1,23,5,6]))

# def findMaxValue(arr):
#     if len(arr)==1:
#         return arr[0]
#     temp = arr.pop(0)
#     for i in range(len(arr)):
#         if arr[i]>temp:
#             return findMaxValue(arr[i:])
#     return temp
#
# print(findMaxValue([33,44,556,2343242342,44,13,2443,3,342423]))


a=[2,3,4,5]+[4,5,7,8,4]
print(a)


