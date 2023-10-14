class bubble_sort():
    def __init__(self,unsorted_list:list):
        self.list = unsorted_list
    def sort(self):
        alive = True # if there is no change then keep going 
        while alive:
            alive = False
            for i in range(len(self.list)):
                if i <len(self.list)-1:
                    current = self.list[i]
                    if self.list[i+1] < self.list[i]:
                        self.list[i] = self.list[i+1]
                        self.list[i+1] = current
                        alive = True
    def output(self):
        return self.list
                        
                        
bs = bubble_sort([54,32,1,87,56,98])
bs.sort() 
print(bs.output())     
            
                
        