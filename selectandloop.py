numbers = '123445'


num = '10723989'
ln = len(num)

not_listed = []

for i in range(ln):
    if num[i] in numbers:
        print(num[i])
    elif num[i] not in numbers:
        not_listed.append(num[i])
        
print(*sorted(not_listed, reverse=False), 'is not in the numbers list')