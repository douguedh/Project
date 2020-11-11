#Space Invaders - Part 10
#Sound (MacOSX / Linux Only)
#Python 2.7 on Mac
import turtle
import os
import math
import random
from turtle import tracer
import platform

if platform.system() == "Windows":
	try:
		import winsound
	except:
		print("Winsound module not available.")

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)

#Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 15

#Choose a number of enemies
number_of_enemies = 30
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

enemytx = -225
enemyty = 250
enemyn = 0

for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = enemytx  + (50 * enemyn)
	y = enemyty
	enemy.setposition(x, y)
	enemyn += 1
	if enemyn == 10:
		enemyty -= 50
		enemyn = 0


enemyspeed = 0.2



#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 10

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
    player.speed = -1

def move_right():
    player.speed = 1

def move_player():    
	x = player.xcor()
	x += player.speed
	if x < -280:
		x = - 280
	if x > 280:
    		x = 280
	player.setx(x)

def fire_bullet():
	#Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		play_sound("laser.wav")
		bulletstate = "fire"
		#Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()


def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
	                     math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 15:
		return True
	else:
		return False

def play_sound(sound_file, time = 0):
		if platform.system() == "Windows":
   			winsound.PlaySound(sound_file, winsound.SND_ASYNC)
		if platform.system() == "Linux":
			os.system("aplay -q {}&" .format(sound_file))
		else:
			os.system("afplay {} &" .format(sound_file))
		if time > 0:
    			turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time*1000))


#Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")
play_sound("bgm.mp3", 119)


#Main game loop
while True:
	wn.update()
	move_player()

	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1

		if enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1

		#Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			play_sound("explosion.wav")
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			enemy.setposition(0, 10000)
			#Update the score
			score += 10
			scorestring = "Score: {}" .format(score)
			score_pen.clear()
			score_pen.write(scorestring, False, align="left",
			                font=("Arial", 14, "normal"))

		if isCollision(player, enemy):
			play_sound("explosion.wav")
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"


wn.mainloop() 
