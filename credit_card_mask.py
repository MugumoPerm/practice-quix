def maskify(cc):
    a = []
    b = []
    ln = len(cc)
    if ln <= 4:
        return cc
    for i in range(0, ln-4):
        hash = '#'
            
    a = (hash*i + cc[ln-4:])
    # a = [a]
    return a

    
print(maskify('SF$SDfgsd2eA'))