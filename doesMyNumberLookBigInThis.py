

numbers = [3,7,1]

number = int(str(numbers))

ln = len(numbers)
# print(ln)
add = []

for i in range(ln):
    
    numbr = (numbers[i]**ln)

    add.append(numbr)
    # print(add)
s = sum(add)

if s == number:
    print("yes")


print(s)