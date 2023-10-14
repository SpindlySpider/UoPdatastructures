class insertion_sort():
    def __init__(self,unsorted_list:list) :
        self.list = unsorted_list
    def sort(self):
        for i in range(1,len(self.list)): #position 1 for already sorted bits
            j = i-1 #start of the sorted list, left side is sorted list
            current = self.list[i] # current element to sort , one index positoon above the sorted list
            while j >= 0 and current< self.list[j]: 
                #if j is above 0 and sort though sorted list to find right insert position
                self.list[j+1] = self.list[j] # move the element below to above
                self.list[j]=current # set the current value to the right position untill everything is in correct position
                j  -= 1 #decrease j index untill its gone through the entire sorted list
                
                
            
                
    def output(self):
        return self.list
                
                
i = insertion_sort([6,3,10,11,6754,4324,576875,43])
i.sort()
print(i.output())

                