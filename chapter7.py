# Turtleグラフィックスのライブラリをインポート
from turtle import *

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

n = 1 # 次数
length = 400 # 直線の長さ
koch(n, length)
