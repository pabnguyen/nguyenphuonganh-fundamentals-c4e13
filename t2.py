from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']


for n in range(5):
    color(colors.pop(0))
    begin_fill()

    for i in range(2):

        forward(60)
        left(90)

        forward(120)
        left(90)

    forward(60)
    end_fill()



mainloop()
