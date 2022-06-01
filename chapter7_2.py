from turtle import *

# 2次の2分木（左の枝だけ3次に）
def tree(length, angle):

    forward(length)

	# 左の枝
    left(angle)
    next_left_length = 0.8 * length # 枝の長さを0.8倍

    #----------
    # 左の枝だけ2次に変更
    forward(next_left_length)

	# 左の枝
    left(angle)
    next_next_left_length = 0.8 * next_left_length # 枝の長さを0.8倍
    forward(next_next_left_length)
    backward(next_next_left_length)

	# 右の枝
    right(angle * 2)
    next_next_right_length = 0.5 * next_left_length # 枝の長さを0.5倍
    forward(next_next_right_length)
    backward(next_next_right_length)

	# 始点に戻る
    left(angle)
    backward(next_left_length)
    #----------

	# 右の枝
    right(angle * 2)
    next_right_length = 0.5 * length # 枝の長さを0.5倍
    forward(next_right_length)
    backward(next_right_length)

	# 始点に戻る
    left(angle)
    backward(length)

speed(0)
penup()
goto(100, -200)
setheading(90)
pendown()

length = 150 # 枝の長さ
angle = 30 # 分岐の角度
tree(length, angle)
