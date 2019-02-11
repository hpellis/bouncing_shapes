from moving_shapes import *

frame=Frame(400,400)
numshapes=3
shapes=[]

size=60

for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
    
for i in range(300):
    for shape in shapes:
        shape.move_tick()
        
frame.close()        