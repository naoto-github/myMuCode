from random import *

WIDTH = 640
HEIGHT = 480

music.play("bgm")

ufo_list = []
animation_list = []
finish_flg = False

for i in range(10):
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    ufo = Actor("ufo1", (x, y))
    ufo.alive = True
    ufo_list.append(ufo)

for ufo in ufo_list:
    target_x = randint(0, WIDTH)
    target_y = randint(0, HEIGHT)
    animation = animate(ufo, pos=(target_x, target_y), tween="linear", duration=5)
    animation.ufo = ufo
    animation_list.append(animation)

def draw():

    screen.fill("white")

    for ufo in ufo_list:
        if ufo.alive == True:
            ufo.draw()

    if finish_flg:
        screen.draw.text("FINISH", center=(WIDTH/2, HEIGHT/2), color="black", fontsize=128)

def update():

    for animation in animation_list:
        if not(animation.running):
            animation.ufo.image = "ufo2"

def on_mouse_down(pos):

    for ufo in ufo_list:
        if ufo.collidepoint(pos) and animation.ufo.image == "ufo1":
            sounds.scratch_001.play()
            ufo.alive = False

def finish():
    global finish_flg
    finish_flg = True
    music.stop()

clock.schedule(finish, 5)
