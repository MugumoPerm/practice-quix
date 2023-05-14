#program to find a valid walk
#given the directions in array form
#each letter represent a minimum of 1 minute
#@ def function to find a walk of ten minutes
#returns true if the walk is ten minutes


def is_valid_walk(walk):
    distance = len(walk)
    if distance != 10:
        return False
    else:
        front = []
        backwards = []
        back = []
        countT = 0
        countF = 0
        halfDistance = (distance)//2
        for i in range(halfDistance):
            front.append(walk[i])
            backwards.append(walk[halfDistance+i])
        print(front)
        
        for i in range(1, halfDistance+1):
            back.append(backwards[halfDistance-i])
        print(back)
        
        for i in range(0, halfDistance):
            if front[i] == back[i]:
                countF += 1
                print(False)
            else:
                countT += 1
                print(True)
        print(countT)
        print(countF)
        
        if countT == halfDistance:
            return 
        
    
    
print(is_valid_walk(['n','w','n','n','w','w','n','n','w','n']))