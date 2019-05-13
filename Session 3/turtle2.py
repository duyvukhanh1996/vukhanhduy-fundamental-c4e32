from turtle import *
colors = ["red","blue","brown","yellow","grey"]
shape("turtle")
length = 30 * len(colors)
for i in range(len(colors)):
    color(colors[len(colors)-i-1])
    fillcolor(colors[len(colors)-i-1])
    begin_fill()
    for j in range(2):
        forward(length)
        left(90)
        forward(60)
        left(90)
    end_fill()
    length -= 30
mainloop()