class Pop:
    def popping(self,s,t):
        length = len(s)
        h = []
        for i in range(length):
            h.append(s[i])
        for i in range(length):
            if t[i] in h:
                ind = h.index(t[i])
                h.pop(ind)
        if h == []:
            return True 
        else:
            return False
                
                
                
                
solution = Pop()

print(solution.popping("tree", "terr"))