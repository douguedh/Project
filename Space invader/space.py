import turtle
import os
import math
import random
from turtle import delay, distance

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space invaders")
wn.bgpic("background.gif")

turtle.register_shape("foguete.gif")
turtle.register_shape("invaders.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()  
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score  to 0
score= 0
#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "score: %s" %score
score_pen.write(scorestring, False,align="left",font=("arial", 14, "normal"))
score_pen.hideturtle()



player = turtle.Turtle()
#player.color("black")
player.shape("foguete.gif")
player.pensize(width=5)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
    
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invaders.gif")
    enemy.penup()
    enemy. speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global  bulletstate
    if bulletstate == "ready":
        os.system("afplay laser.wav&")
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2 )+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left, "a" )
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "d")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(fire_bullet, "w")



while True:

    for enemy in enemies: 
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in  enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            os.system("soundcollision.wav")
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #update score
            score += 10
            scorestring = "score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False,align="left",font=("arial", 14, "normal"))
        
        if isCollision(player, enemy):
            os.system("soundcollision.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    
    #move the bullet
    if bulletstate == "fire":
        y =bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = raw_input("input to finish")