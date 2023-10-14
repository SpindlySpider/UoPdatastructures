class queue():
    def __init__(self):
        self.list = []
    def enqueue(self,item_to_append):
        self.list.append(item_to_append)
    def dequeue(self):
        self.list.pop(0)
    def peek(self):
        return self.list[0]
    def length(self):
        return len(self.list)
    
    def __str__(self) :
        tempstr= ""
        for i in self.list:
            tempstr = tempstr + str(i) + "," 
            
        return tempstr