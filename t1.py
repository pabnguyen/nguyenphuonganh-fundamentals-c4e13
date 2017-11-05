from turtle import *
speed(-1)

color = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(3,8):
    for _ in range(i):
        EdgeColor = i - 3
        pencolor(color[EdgeColor])
        forward(100)
        left(360/i)


mainloop()
