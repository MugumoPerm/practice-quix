s = ['p', 'e', 'r', 'm', 'p']
length = len(s)

left = 0
right = length-1

for i in range(length):
    if s[left+i] == s[right-i]:
        print(True)
    else:
        print(False)
        break