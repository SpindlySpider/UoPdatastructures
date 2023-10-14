
def binary_Search(sorted_list:list,item:int|float):
    not_found= True
    List = sorted_list
    while not_found:
        middle_index = int((len(List)-1)/2)
        if len(List) == 0:
            return False
        if item == List[middle_index]:
            not_found = False
        elif item < List[middle_index]:
            #item is in left hand side
            List = List[0:middle_index]
        elif item > List[middle_index]:
            #right hand side 
            List= List[middle_index:-1]
        else:
            return "item not in list"
    return True
            
            
            
print(binary_Search([1,2,3,4,5,6,7,8,9,10,12,345],8))