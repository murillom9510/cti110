import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


# square
for i in range(4):
    t.forward(50)
    t.left(90)

# triangle
for i in range(3):
    t.forward(175)
    t.left(120)

win.mainloop()  


