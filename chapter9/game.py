WIDTH = 640 # ウィンドウの幅
HEIGHT = 480 # ウィンドウの高さ

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

def on_mouse_down():
    global flg
    flg = True

