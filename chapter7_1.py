from turtle import *

# 1次のコッホ曲線
def koch1(length):
    next_length = length / 3

    forward(next_length)

    #----------
    # 最初の辺だけ2次に変更
    """
    next_next_length = length / 3 / 3
    forward(next_next_length)
    left(60)
    forward(next_next_length)
    right(120)
    forward(next_next_length)
    left(60)
    forward(next_next_length)
    """
    #---------

    left(60)
    forward(next_length)
    right(120)
    forward(next_length)
    left(60)
    forward(next_length)

speed(0)
penup()
goto(-200, 0)
pendown()

length = 400 # 直線の長さ
koch1(length)
