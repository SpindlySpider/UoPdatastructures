from python_queue import *

def fibonacci_iteritive(n:int)->int:
    if n<=2:
        return 1 
    counter = 2 # we will not be using 0th index instead counting from 1
    number_queue = queue() # will only ever have 2 elements in it
    number_queue.enqueue(1)
    number_queue.enqueue(2)
    
    while (counter != n):
        temp_number = number_queue.peek()
        number_queue.dequeue()
        number_queue.enqueue(temp_number+number_queue.peek())
        counter +=1
    return number_queue.peek()



for i in range(10):
    print(fibonacci_iteritive(i))