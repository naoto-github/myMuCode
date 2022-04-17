WIDTH = 640 # ウィンドウの幅
HEIGHT = 480 # ウィンドウの高さ

player = Actor("player_idle", (320, 240))

def draw():
    screen.fill("white") # screen.fill((255, 255, 255))でもOK
    player.draw()

walk_images = ["player_walk1", "player_walk2"]
walk_counter = 0
def walk(dx, dy):
    global walk_counter
    player.image = walk_images[walk_counter]
    player.x += dx
    player.y += dy
    walk_counter += 1
    walk_counter = walk_counter % len(walk_images)

def update():
    if keyboard.right:
        walk(10, 0)
    elif keyboard.left:
        walk(-10, 0)
    elif keyboard.up:
        walk(0, -10)
    elif keyboard.down:
        walk(0, 10)
