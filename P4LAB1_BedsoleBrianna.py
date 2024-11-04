import turtle

def main():
    t = turtle.Turtle()
    t.pensize(4)
    t.speed(4)
    
    t.pencolor("cyan")
    for _ in range(4):
        t.forward(100)
        t.right(90)
    
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    
    t.pencolor("pink")
    for _ in range(3):
        t.forward(100)
        t.left(120)
    
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
