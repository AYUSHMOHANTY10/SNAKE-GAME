#Importing libraries
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(100, 0)]
aim = vector(0, -10)

#Creating functions
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'black')
        update()
        return

    snake.append(head)
    if head == food:
        print('Snake:', len(snake))
        if len(snake)==10:
            print("KEEP IT UP")
        if len(snake)==50:
            print("YOU ARE DOING GREAT")
        if len(snake)==100:
            print("AND THAT'S A CENTURY")
        if len(snake)==500:
            print("PRO OE WOT")
        if len(snake)==1000:
            print("YOU ARE A MASTER")
        #Next food particle place
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'red')
        square(head.x, head.y, 9, 'brown')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Code
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
