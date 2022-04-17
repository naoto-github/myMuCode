from random import *

WIDTH = 640 # ウィンドウの幅
HEIGHT = 480 # ウィンドウの高さ

def draw():
    screen.fill("white")

    screen.blit("tree1", (0, 0))
    screen.blit("tree2", (300, 0))

    for i in range(10):
        x = randint(100, 240)
        y = randint(60, 200)
        screen.draw.filled_circle((x, y), 10, (255, 0, 0))
        screen.draw.line((x, y-5), (x, y-15), (0, 0, 0))

    for i in range(10):
        x = randint(400, 540)
        y = randint(60, 200)
        screen.draw.filled_circle((x, y), 10, (255, 255, 0))
        screen.draw.line((x, y-5), (x, y-15), (0, 0, 0))

"""
dog = Actor("dog", (100, 100))

def draw():
    screen.fill("white")
    #screen.blit(images.dog, (120, 200))
    dog.draw()
    animate(dog, pos=(300, 300))
"""


"""
flg = False

x1 = 320
y1 = 240
speed1 = 5

x2 = 320
y2 = 240
speed2 = 5
"""

"""
def draw():
    screen.fill("white")
    screen.draw.filled_circle((x1, y1), 10, "red")
    screen.draw.filled_circle((x2, y2), 10, "blue")
"""

"""
def update():
    global x1, y1, speed1
    global x2, y2, speed2

    if flg:
        x1 = x1 + speed1
        if x1 >= WIDTH or x1 <= 0:
            speed1 = speed1 * -1

        y2 = y2 + speed2
        if y2 >= HEIGHT or y2 <= 0:
            speed2 = speed2 * -1

def on_key_down(key):
    global flg
    if key == keys.SPACE:
        flg = True
"""

"""
def update():
    global x, y, speed
    x = x + speed

    if x >= WIDTH or x <= 0:
        speed = speed * -1
"""

"""
# 60fpsで更新
def update():
    global x, y
    x = x + 1
"""

"""
def draw():
    # 背景色が白のスクリーン
    screen.fill("white")

    # 始点(50, 50)から終点(200, 50)に黒色の直線を描く
    screen.draw.line((50, 50), (200, 50), "black")

    # 左上の座標(50, 150)，幅100，高さ100の赤色の正方形を描く
    screen.draw.rect(Rect((50, 150), (100, 100)), "red")

    # 左上の座標(50, 300)，幅100，高さ100，緑色の塗りつぶしの正方形を描く
    screen.draw.filled_rect(Rect((50, 300), (100, 100)), "green")

    # 中心(300, 150)，半径50，青色の正方形を描く
    screen.draw.circle((300, 150), 50, "blue")

    # 中心(300, 300)，半径50，黄色の塗りつぶしの正方形を描く
    screen.draw.filled_circle((300, 300), 50, "yellow")

    # 左上の座標(400, 150)，フォントサイズ24，黒色の文字列「ABC」を描く
    #screen.draw.text("ABC", (400, 150), color="black")

    # 左上の座標(400, 300)，フォントサイズ32，黒色の文字列「あいう」を描く
    # IPAexフォント https://moji.or.jp/ipafont/
    #screen.draw.text("あいう", (400, 300), fontname="ipaexg", color="black", fontsize=32)
"""
