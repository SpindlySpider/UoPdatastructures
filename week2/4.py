
def linear_search(unsorted_list:list,item:any):
    for list_item in unsorted_list:
        if list_item == item:
            return item
    return "item is not in list"

