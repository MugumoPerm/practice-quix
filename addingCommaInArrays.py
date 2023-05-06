num = 371



numb = str(num)

new_numb = ""
nmb = []
for i, digit in enumerate(numb):
    if i % 1 == 0 and i != 0:
        new_numb += ","
    new_numb += digit

print(new_numb)
ln = len(new_numb)

for i in range(0,ln, 2):
    n= new_numb[i]
print(ln)