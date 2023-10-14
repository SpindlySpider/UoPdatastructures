def binary_Search(sorted_list:list,item:int|float):
    List = sorted_list
    middle_index = int((len(List)-1)/2)
    if len(List) == 0:
        return False
    if item == List[middle_index]:
        return True
    elif item < List[middle_index]:
        #item is in left hand side
        if binary_Search(List[0:middle_index],item):
            return True
        return False
    elif item > List[middle_index]:
        #right hand side 
        if binary_Search(List[middle_index:-1],item):
            return True
        return False
    else:
        return False
    
    
print(binary_Search([1,2,3,4,5,6,7,8,9,10,12,345],8))