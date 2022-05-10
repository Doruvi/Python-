import turtle

#Screen interface
wn = turtle.Screen()
wn.title("test pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .15
ball.dy = .15

#function
def Paddle_a_up():
    y = paddle_a.ycor()
    y += float(30)
    paddle_a.sety(y)

def Paddle_a_down():
    y = paddle_a.ycor()
    y -= float(30)
    paddle_a.sety(y)

def Paddle_b_up():
    y = paddle_b.ycor()
    y += float(30)
    paddle_b.sety(y)

def Paddle_b_down():
    y = paddle_b.ycor()
    y -= float(30)
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(Paddle_a_up, "w")
wn.onkeypress(Paddle_a_down, "s")

wn.onkeypress(Paddle_b_up, "Up")
wn.onkeypress(Paddle_b_down, "Down")

    

#main loop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checkking
    
