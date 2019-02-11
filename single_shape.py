from moving_shapes import *

frame=Frame(400,400)

shape1=Square(frame, 100)

for i in range (100):
    shape1.move_tick()
    
frame.close()
