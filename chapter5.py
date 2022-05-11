# Turtleグラフィックスのライブラリをインポート
from turtle import *
import numpy as np

"""
print(type(10))
print(type(0.1))
print(type("abc"))
print(type(True))

x = "100"
y = "3.14"
z = "True"

print(type(x))
print(type(y))
print(type(z))
"""

"""
# 消費税の計算
price = input("金額を入力してください >>")
price = price * 1.1
print(price)
"""

"""
# 消費税の計算
price = input("金額を入力してください >>")
price = int(price) # str型からint型へ変換
price = price * 1.1
print(price)
"""

"""
# 消費税の計算
price = input("金額を入力してください >>")
price = int(price) # str型からint型へ変換
price = price * 1.1 # int型からfloat型に変換
#price = int(price) # float型からint型に変換
print(price)
"""

"""
x = input("xを入力してください >>")
print(type(x))
print(x)

x = int(x)
print(type(x))
print(x)
"""

"""
radius = input("radiusを入力してください >>")
radius = int(radius)
speed(0)
circle(radius)
"""

"""
print(np.pi)

def calcArea():
    radius = 3
    area = radius ** 2 * np.pi
    print(area)

calcArea()
"""

"""
# 関数を定義
def calcArea(radius):
	area = radius ** 2 * np.pi # 半径*半径*円周率
	print(area)
	
# 関数の呼び出し
calcArea(5) # -> 28.274333882308138

# 関数を定義
def calcArea(radius):
	area = radius ** 2 * np.pi
	return area
	
# 関数の呼び出し
area3 = calcArea(3) # -> 28.274333882308138
area5 = calcArea(5) # -> 78.53981633974483
print(area3 + area5)
"""

"""
def drawPolygon(x, y, vertex):

  penup()
  goto(x, y) # 始点の座標はx,y
  pendown()

  sum = 180 * (vertex - 2) # 内角の和
  angle = sum / vertex # 頂点の角度

  for i in range(vertex):
    forward(200)
    right(180 - angle)

drawPolygon(-100, 100, 4)
drawPolygon(-100, 173, 6)
"""

"""
speed(0)

def drawPolygon(x, y, vertex, length):

  penup()
  goto(x, y) # 始点の座標はx,y
  pendown()

  sum = 180 * (vertex - 2) # 内角の和
  angle = sum / vertex # 頂点の角度

  for i in range(vertex):
    forward(length)
    right(180 - angle)

vertex = input("頂点数を入力してください >>")
vertex = int(vertex)

length = input("辺の長さを入力してください >>")
length = int(length)

drawPolygon(0, 150, vertex, length)
"""

"""
penup()
goto(0, -300)
pendown()
circle(300)
"""

"""
print(np.cos(np.radians(45))) # 余弦 -> 0.0
print(np.sin(np.radians(45))) # 正弦 -> 1.0

print(np.cos(np.radians(90))) # 余弦 -> 0.0
print(np.sin(np.radians(90))) # 正弦 -> 1.0
"""

def drawInscribedPolygon(vertex):

    radius = 300

    penup()
    goto(radius, 0)
    pendown()

    for i in range(vertex):
        angle = (360 / vertex) * (i+1)
        x = radius * np.cos(np.radians(angle))
        y = radius * np.sin(np.radians(angle))
        goto(x, y)

vertex = input("頂点数を入力してください >>")
vertex = int(vertex)
drawInscribedPolygon(vertex)
