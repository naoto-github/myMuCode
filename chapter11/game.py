from random import *

WIDTH = 640
HEIGHT = 480

counter = 0
ufo_list = []

music.play("bgm")

def makeUFO():

    # 乱数でUFOの初期座標を設定
    x = randint(0, 640)
    y = randint(0, 480)
    ufo = Actor("ufo1", center=(x, y))

    # 乱数でUFOの目的座標を設定
    x2 = randint(0, 640)
    y2 = randint(0, 480)
    animate(ufo, pos=(x2, y2), tween="linear", duration=3)

    # UFOをリストに追加
    ufo_list.append(ufo)

    # サウンドを再生
    sounds.open_001.play()

# 1秒ごとにmakeUFO()を呼び出す
clock.schedule_interval(makeUFO, 1)

def draw():
    screen.fill("white")

    for ufo in ufo_list:
        ufo.draw()

    if counter >= 10:
        screen.draw.text("FINISH", center=(WIDTH/2, HEIGHT/2), color="black", fontsize=128)

        if music.is_playing("bgm"):
            music.stop()
            sounds.confirmation_004.play()

def update():

    if len(ufo_list) == 10:
        clock.unschedule(makeUFO)

def on_mouse_down(pos):
    global counter
    for ufo in ufo_list:
        if ufo.collidepoint(pos):
            sounds.scratch_001.play()

            if ufo.image == "ufo1":
                ufo.image = "ufo2"
                counter = counter + 1


"""
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
"""
