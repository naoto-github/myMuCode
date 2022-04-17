from random import *

WIDTH = 640 # ウィンドウの幅
HEIGHT = 480 # ウィンドウの高さ
flg = False

class Apple:

	# コンストラクタ（引数で値を設定）
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

# 引数に値を渡す
apple1 = Apple(320, 0, 1, "green")
apple2 = Apple(480, 0, 1, "pink")

def draw():
    screen.fill("white")
    apple1.paint()
    apple2.paint()

def update():
    if flg:
        apple1.fall()
        apple2.fall()

def on_mouse_down():
    global flg
    flg = True

"""
class Apple:

    def __init__(self, x, y, speed, color, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        self.visible = False

    def paint(self):
        if self.visible:
            screen.draw.filled_circle((self.x, self.y), self.radius, self.color)
            screen.draw.line((self.x, self.y-5), (self.x, self.y-15), "black")

    def fall(self):
        if self.visible:
            self.y = self.y + self.speed
            self.speed = self.speed + 0.05

apple_list = []
for i in range(100):

    r = randint(0, 2)
    if r == 0:
        color = "red"
        radius = 8
    elif r == 1:
        color = "blue"
        radius = 10
    else:
        color = "green"
        radius = 12

    x = randint(0, 640)
    apple = Apple(x, 0, 1, color, radius)
    apple_list.append(apple)

def draw():
    screen.fill("white")

    if flg:
        for apple in apple_list:

            if random() < 0.001:
                apple.visible = True

            apple.paint()

def update():
    if flg:
        for apple in apple_list:
            apple.fall()

def on_mouse_down():
    global flg
    flg = True
"""

"""
x = 320
y = 0
speed = 1

x2 = 160
y2 = 0
speed2 = 1

flg = False

def draw():
    screen.fill("white") # screen.fill((255, 255, 255))でもOK

    # 赤いリンゴ
    screen.draw.filled_circle((x, y), 10, "red")
    screen.draw.line((x, y-5), (x, y-15), "black")

    # 青いリンゴ
    screen.draw.filled_circle((x2, y2), 10, "blue")
    screen.draw.line((x2, y2-5), (x2, y2-15), "black")

def update():
    global x, y, speed
    global x2, y2, speed2
    if flg:
        y = y + speed
        y2 = y2 + speed2
        speed = speed + 0.05
        speed2 = speed2 + 0.05

def on_mouse_down():
    global flg
    flg = True
"""
