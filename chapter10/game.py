from random import *

WIDTH = 640
HEIGHT = 480

player = Actor("player_stand", midbottom=(320, 480))
walk_speed = 5
jump_speed = [1, 2, 3, 4, 5, 4, 3, 2, 1]

def stand():
    player.image = "player_stand"

def walk_left():
    player.x = player.x - walk_speed
    player.image = "player_walk1"

def walk_right():
    player.x = player.x + walk_speed
    player.image = "player_walk1"

def catch():
    player.image = "player_hang"

class Apple:

    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color

    def paint(self):
        screen.draw.filled_circle((self.x, self.y), 10, self.color)
        screen.draw.line((self.x, self.y-5), (self.x, self.y-15), "black")

    def fall(self):
        self.y = self.y + self.speed
        self.speed = self.speed + 0.05

x = randint(0, 640)
apple = Apple(x, 0, 1, "green")

def draw():
    screen.fill("white")
    player.draw()
    apple.paint()

def update():

    if keyboard.left:
        walk_left()
    elif keyboard.right:
        walk_right()
    elif keyboard.up:
        catch()
    else:
        stand()

    apple.fall()


