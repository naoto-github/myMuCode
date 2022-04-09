# Turtleグラフィックスのライブラリをインポート
from turtle import *

"""
def mouse_event(x, y):
    penup()
    goto(x, y)
    pendown()
    dot(10)
    penup()

 # マウスの左ボタン
onscreenclick(mouse_event)
"""

def mouse_left(x, y):
    penup()
    goto(x, y)
    pendown()
    color("red")
    dot(10)
    penup()

def mouse_right(x, y):
    penup()
    goto(x, y)
    pendown()
    color("blue")
    dot(10)
    penup()

# マウスの左ボタン
onscreenclick(mouse_left, btn=1)

# マウスの右ボタン（トラックパッドの場合は2本指でタップ）
onscreenclick(mouse_right, btn=2)

