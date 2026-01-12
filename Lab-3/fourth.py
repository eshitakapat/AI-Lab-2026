# wap to find the index of a given element in a list

def find_index(lst, element):
    for i, value in enumerate(lst):
        if value == element:
            return i
    return -1