# Turtleグラフィックスのライブラリをインポート
from turtle import *

"""
# n次のコッホ曲線
def koch(n, length):
    if n == 0:
        forward(length)
        return # 再帰の終了

    # n-1次の直線の長さ
    next_length = length / 3

    koch(n-1, next_length)
    left(60)
    koch(n-1, next_length)
    right(120)
    koch(n-1, next_length)
    left(60)
    koch(n-1, next_length)

speed(0)
penup()
goto(-200, 0)
pendown()

n = 3 # 次数
length = 400 # 直線の長さ
koch(n, length)
"""

"""
# n次の2分木
def tree(n, length, angle):
    if n == 0:
        return

    forward(length)
    left(angle)
    next_left_length = 0.8 * length
    tree(n-1, next_left_length, angle)
    right(angle * 2)
    next_right_length = 0.5 * length
    tree(n-1, next_right_length, angle)
    left(angle)
    backward(length)

speed(0)
penup()
goto(100, -200)
setheading(90)
pendown()

n = 6
length = 150
angle = 30
tree(n, length, angle)
"""

# n次のコッホ曲線
def koch(n, length):
    if n == 0:
        forward(length)
        return # 再帰の終了

    # n-1次の直線の長さ
    next_length = length / 3

    koch(n-1, next_length)
    left(90)
    koch(n-1, next_length)
    right(90)
    koch(n-1, next_length)
    right(90)
    koch(n-1, next_length)
    left(90)
    koch(n-1, next_length)

speed(0)
penup()
goto(-200, 0)
pendown()

n = 2 # 次数
length = 400 # 直線の長さ
koch(n, length)
