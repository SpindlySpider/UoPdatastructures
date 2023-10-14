def greatest_common_divisor(number1:int,number2:int)->int:
    if number2 == 0:
        return number1
    else:
        return greatest_common_divisor(number2, number1 % number2)
    

number1=342432
number2=56
print(f"{number1}and {number2} greatest common factor is {greatest_common_divisor(number1,number2)}")
