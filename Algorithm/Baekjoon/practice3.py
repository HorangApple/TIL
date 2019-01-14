# 아래에 코드를 작성해주세요.
import turtle
window = turtle.Screen()
window.bgcolor('red')

ggobugi = turtle.Turtle()
ggobugi.color("yellow")
ggobugi.shape("turtle")
ggobugi.speed(10)
for i in range(10):
    for i in range(4):
        ggobugi.forward(100)
        ggobugi.right(90)
    ggobugi.left(100)
    ggobugi.right(20)    

window.exitonclick()
