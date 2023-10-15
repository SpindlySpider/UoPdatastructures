def merge_sort(items:list):
    if len(items)<=1:
        return items
    item1 = merge_sort(items[0:len(items)//2]) #split the lists in the middle into two diffrent lists
    item2 = merge_sort(items[len(items)//2:len(items)])
    #run sorting operation

    return merge_items(item1,item2)

def merge_items(item1:list,item2:list):
    index1 =0 
    index2 = 0
    merged_items =[]
    while index1 < len(item1) and index2 < len(item2):
        if item1[index1] < item2[index2]:
            merged_items.append(item1[index1])
            index1 +=1
        else:
            merged_items.append(item2[index2])
            index2 += 1
    merged_items.extend(item1[index1:])
    merged_items.extend(item2[index2:])
    return merged_items
    


print(merge_sort([1,2,5,4,2,6,8,5,3,6,912,432,765,123]))
    
    