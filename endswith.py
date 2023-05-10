def solution(text, ending):
    lnw = len(ending)
    lnt = len(text)
    if lnw > lnt:
        return False
    count = 0
    if text[len(text)-1] == ending[lnw-1]:
        pass
        for i in range(0, len(ending)):
            
            if (ending[lnw-1-i] == text[lnt-i-1]):
                count += 1
            else:
                break
        print(count, lnw)
        if count == lnw:
            return True
        else:
            return False
        
    
    else:
        return False
    
print(solution("permo", "kkermo"))