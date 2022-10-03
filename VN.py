import turtle
from turtle import *
import time
bgcolor('black')
setup(680, 610)
speed(1)
penup()
goto(-55,25)
pendown()
color('yellow')
begin_fill()
for i in range(5):
	forward(120)
	right(144)
end_fill()
bgcolor('red')
turtle.getscreen()._root.mainloop()