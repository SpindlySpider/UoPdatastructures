class selection_sort():
    def __init__(self):
        self.list1 = []
        self.list2 = []
    def fill_queue(self,queue1):
        self.list1 = queue1
    def sort(self):
        while len(self.list1) != 0:
            self.list2.append(min(self.list1))
            self.list1.pop(self.list1.index(min(self.list1)))
    def output(self):
        return self.list2
        
        

unsorted_list = [-1,6,4,3,5,8,7,10,3432]
selec = selection_sort()
selec.fill_queue(unsorted_list)
selec.sort()
print(selec.output())