# wap to remove duplicates from a list

list1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

def remove_duplicates(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2