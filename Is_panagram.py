def is_pangram(s):
    count = 0
    alph = []
    lns = len(s)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lna = len(alphabet)
    if lns< lna:
        lna = lns
    if s[1] not in alphabet:
        return False
    else:
        for i in range(lna):
                for j in range(lns):
                    
                    #print(alphabet[i], s[j])
                    if s[j] is alphabet[i]:
                        alph.append(s[j])
    print(alph)
    print(alph.index(alphabet[5]))
    print(len(alph), lns)
    
    # for i in range(len(alph)):
    #     if  alph[i] in alphabet[i]:
    #         print(True)
    #         count += 1
    #     else:
    #         return False
    # print(count)
    # if count == len(alph):
    #     return True    
                    
    
    
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))