# Turtleグラフィックスのライブラリをインポート
from turtle import *

penup()
goto(-200, 0)
pendown()

color(1, 0, 0)
forward(100)

color(0, 1, 0)
forward(100)

color(0, 0, 1)
forward(100)

color(1, 0.7, 0.8)
forward(100)

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
