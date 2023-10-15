def palindrome(string:str)->bool:
    if len(string) <= 1:
        return False
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
    
    
print(palindrome("aa"))


    