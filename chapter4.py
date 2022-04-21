# Turtleグラフィックスのライブラリをインポート
from turtle import *

# 乱数生成のためのモジュールをインポート
from random import *

"""
# 0以上1未満の乱数
for i in range(10):
    print(random())

# 範囲を指定した乱数
for i in range(10):
    print(uniform(1, 5))

# 範囲を指定した乱数（整数）
for i in range(10):
    print(randint(1, 5))

# 正規分布に従う乱数
for i in range(10):
    print(normalvariate(0, 5))
"""

"""
speed(0)
for i in range(100):
    penup()
    x = uniform(-300, 300)
    y = uniform(-300, 300)
    goto(x, y)
    pendown()
    dot(10)
"""

"""
speed(0)
for i in range(100):
    penup()
    x = normalvariate(0, 100)
    y = normalvariate(0, 100)
    goto(x, y)
    pendown()
    dot(10)
"""

"""
x = 3
print(x == 3)
print(x != 3)
print(x > 3)
print(x >= 3)
print(x < 4)
print(x <= 2)

x = "A"
print(x == "B")
print(x != "B")
print(x > "B")
print(x >= "B")
print(x < "B")
print(x <= "B")

# 論理積
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# 論理積
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 否定
print(not(True))
print(not(False))

x = 20
y = 30
print((x > 10) and (y <= 30))
print((x > 20) or (y < 40))
print(not(x != 20) and not(y == 30))
"""

"""
# xとyは自然数とする
x = 3
y = 3
if x > y:
    print(f"{x}は{y}より大きい")
elif x < y:
    print(f"{x}は{y}より小さい")
else:
    print(f"{x}と{y}は等しい")
"""

"""
speed(0)
for i in range(100):
    penup()
    x = uniform(-300, 300)
    y = uniform(-300, 300)
    goto(x, y)
    pendown()
    if position()[0] > 0:
        color("red")
        dot(10)
    else:
        color("black")
        dot(10)
"""

speed(0)
for i in range(100):
    penup()
    x = uniform(-300, 300)
    y = uniform(-300, 300)
    goto(x, y)
    pendown()
    if position()[0] > 0 and position()[1] > 0:
        color("red")
    elif position()[0] > 0 and position()[1] <= 0:
        color("blue")
    elif position()[0] <= 0 and position()[1] <= 0:
        color("green")
    elif position()[0] <= 0 and position()[1] > 0:
        color("pink")

    dot(10)
