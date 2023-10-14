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

def fibonacci_recursive(n:int, number1=1,number2=1,counter =3)->int:
    # use the nth paramater to see what number we need to get to
    if n<=2:
        return 1 
    elif n != counter: # if we have not reached the number index we wanted to find
        #print(number1,number2)
        temp_number = number2
        number2 += number1
        number1 = temp_number
        counter += 1 
        return fibonacci_recursive(n,number1,number2,counter)
    else:
        return number1+number2

for i in range(1,10):
    print(fibonacci_iteritive(i),"#",fibonacci_recursive(i))