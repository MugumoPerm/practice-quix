def DDA(x1, x2, y1, y2):
   # Get the steps
   dx = x2-x1
   dy = y2-y1

   if dx > dy:
       step = dx
   else:
        step = dy
   print(step)
   
   # Calculate the y and x increment
   y_inc = dy/step
   x_inc = dx/step

   #create a loop with a range of steps while adding the increment values starting from (x1, y1)
   for i in range(step):
        x1 += x_inc
        y1 += y_inc
        print(x1, y1)

# Get the two points
x1,y1 = (5,6)
x2,y2 = (30,28)

DDA(x1, x2, y1, y2)
