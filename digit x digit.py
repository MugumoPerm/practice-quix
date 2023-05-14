#this function returns the square root of each digit in the number
# @param num

def square_digits(num):
    square_ = []
    number = str(num)
    ln = len(number)
    if num == 0:
        return 0
    for i in range(ln):
        square = (int(int(number[i])*int(number[i])))
        
        square_.append(square)
    string_number = ''
    for i in square_:
        print(i)
        string_number +=str(i)
        
    return(int(string_number))

        
        
print(square_digits(9119))