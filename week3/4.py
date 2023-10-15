def quick_sort(items:list):
    # keep indexs of the each group
    if len(items) <=1:
        return items
    pivot = items[len(items)//2] # piviot around last 
    item1 = []
    middle = []
    item2 = []
    for i in items:
        if i<pivot:
            item1.append(i)
    for i in items:
        if i == pivot:
            middle.append(pivot)
    for i in items:
        if i > pivot:
            item2.append(i)
    return quick_sort(item1)+middle+quick_sort(item2)


print(quick_sort([5,3245243,6,5,3,48,43,23,6,38,34]))
    