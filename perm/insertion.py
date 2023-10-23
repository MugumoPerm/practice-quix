#insertion 

values = [1,2,3,4,5]

length = len(values)

ind = 2
v = 50

for i in range(length):
    if i == 2:
        values[i] = values[v]   
print(values)
