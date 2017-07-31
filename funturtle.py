import turtle
turtle.shape('turtle')
turtle.goto(0,100)
turtle.shape('turtle')
turtle.goto(100,100)
turtle.shape('turtle')
turtle.goto(100,0)
turtle.shape('turtle')
turtle.goto(0,0)


turtle.penup()
turtle.goto(150,150)
turtle.pendown()


turtle.shape('turtle')
turtle.goto(150,200)
turtle.goto(200,150)
turtle.goto(150,150)






square=turtle.clone()
square.shape('square')



turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
square.goto(1000,1000)
square.goto(300,300)
square.stamp()
square.goto(100,100)




turtle.mainloop()
