def ternary_search(inputList:list,item:any):
    List = inputList
    not_found = True
    while not_found:
        if len(List) == 0:
            return False
        length = (len(List)-1)
        mid1 = length//3
        mid2 = length -(length//3)
        if len(List) == 1 and List[mid1] != item:
            return False
        if List[mid1] == item:
            not_found = False
            return List[mid1]
        elif List[mid2] == item:
            not_found = False
            return List[mid2]
        if item <= List[mid1]:
            List = List[0:mid1]
        elif item >= List[mid2]:
            List = List[mid2:len(List)]
        else:
            List = List[mid1:mid2]
   
print(ternary_search([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ],10)) 