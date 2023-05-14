#This code shows the next traffic light 
#From green, to yellow, to red, to green again
#@param lights

def update_lights(lights):
    light = ['green', 'yellow', 'red', 'green']
    
    for i in range(3):
        if lights == light[i]:
            return(light[i+1])
        
print(update_lights('yellow'))