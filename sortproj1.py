# Python 3.5.2
# Author: Tom Stock
# create sorting algorithms to sort lists in ascending order


list1 = [67, 45, 2, 13, 1, 998 ]
list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def sort_list1(list1):
    for checknum in range(len(list1)-1, 0, -1):
        for i in range(checknum):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i +1] = list1[i + 1], list1[i]

sort_list1(list1)
print(list1)

def sort_list2(list2):
    for number in range(len(list2)-1, 0, -1):
        for i in range(number):
            if list2[i] > list2[i + 1]:
                list2[i], list2[i + 1] = list2[i + 1], list2[i]

sort_list2(list2)
print(list2)

            
