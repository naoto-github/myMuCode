# Turtleグラフィックスのライブラリをインポート
from turtle import *

colormode(255)
bgcolor("yellow")
hideturtle()

penup()
goto(0, 250)
pendown()

pensize(10)
color("red")
right(36)
forward(300)

pensize(10)
color("green")
right(72)
forward(300)

pensize(10)
color("blue")
right(72)
forward(300)

pensize(10)
color("green")
right(72)
forward(300)

pensize(10)
color("red")
right(72)
forward(300)

"""
penup()
goto(-200, 0)
pendown()

colormode(255) # 0〜255の範囲で指定

color(255, 0, 0)
forward(100)

color(0, 255, 0)
forward(100)

color(0, 0, 255)
forward(100)

color(234, 145, 152)
forward(100)
"""

""" 例題1
penup()
goto(200, 200)
right(90)
pendown()
forward(400)
right(90)
forward(400)
right(90)
forward(400)
right(90)
forward(400)
right(90)
"""

"""
print(position()) # タートルの座標
print(heading()) # タートルの向き

forward(200) # 200だけ前進
print(position()) # タートルの座標 -> (200.00,0.00)
print(heading()) # タートルの向き -> 0.0

right(90)
forward(200) # 200だけ前進
print(position()) # タートルの座標 -> (200.00,-200.00)
print(heading()) # タートルの向き -> 270.0

penup()
goto(-200, -200) # タートルを(-200,-200)に移動
pendown()
goto(-200, 200) # タートルを(-200,200)に移動
print(position()) # タートルの座標 -> (-200.00,200.00)
print(heading()) # タートルの向き -> 270.0
"""

"""
# タートルを非表示
hideturtle()

# 描画速度を最速に（標準は6）
speed(0)

goto(0, 0)
goto(200, 200)
goto(200, -200)
goto(-200, -200)
goto(-200, 200)
goto(0, 0)

"""
