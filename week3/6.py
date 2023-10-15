def palindrome(string:str)->bool:
    if len(string) < 1:
        return True
    string_list = []
    for i in range(len(string)):
        string_list.append(string[i])
    reversed = []
    for i in range(len(string)):
        reversed.append(string[len(string)-1-i])
    same_char = True
    for i in range(len(string)):
        if string_list[i] == reversed[i]:
            pass
        else:
            same_char = False
    return same_char

def string_to_list(string:str)->list:
    output = []
    for i in string:
        output.append(i)
    return output

def partition(string:str):
    #going to assume the string cannot be rearanged
    # pass in all versions of the string and keep the ones which return positive form palidome 
    if not string:
        return [[]]
    palindromes = []
    
    
    for i in range(1,len(string)+1):
        # this selects the charaters and tries to find combinations from the charaters on the 
        #right hand side to see if they are palindromes
        preflix = string[:i] 
        for j in partition(string[i:]):
            palindromes.append([preflix]+j)
    return palindromes


def find_palindrome(String:str):
    all_partitions = partition(String)
    palindromes = []
    for items in all_partitions:
        for element in items:
            if palindrome(element) and element not in palindromes:
                palindromes.append(element)
    return palindromes
    
    

print(find_palindrome(""))



