# Turtleグラフィックスのライブラリをインポート
from turtle import *

speed(0)

distance = 10
for index in range(50):
    distance = distance + 10
    forward(distance)
    right(90)

"""
# リスト
xlist = [100, -100, -100, 100]
ylist = [200, 200, -200, -200]
print(xlist) # -> [100, -100, -100, 100]
print(ylist) # -> [200, 200, -200, -200]

# xlistの0番と1番
print(xlist[0]) # -> 100
print(xlist[1]) # -> -100

# xlistの0番と1番
print(ylist[2]) # -> -200
print(ylist[3]) # -> -200

xlist[0] = 300
xlist[1] = -300
xlist[2] = -300
xlist[3] = 300
print(xlist) # -> [300, -300, -300, 300]

# リストの長さ
print(len([1, 2, 3, 4, 5]))
print(len(xlist))

# リストの値の合計
print(sum([1, 2, 3, 4, 5]))
print(sum(xlist))

# 要素の追加
xlist.append(400)
xlist.append(300)
ylist.append(0)
ylist.append(200)
print(xlist)
print(ylist)
"""

"""
goto(xlist[0], ylist[0])
goto(xlist[1], ylist[1])
goto(xlist[2], ylist[2])
goto(xlist[3], ylist[3])
goto(xlist[4], ylist[4])
goto(xlist[5], ylist[5])
"""

"""
# テストの得点
scores = [80, 70, 90, 50, 80]

# for文で要素を取り出す
for data in scores:
	print(data) # 変数dataに値が格納される
"""

"""
total = 0 # 得点の合計
for data in scores:
    total = total + data
    print(total)

print(total / len(scores)) # 要素数で割って平均を算出

for index in range(6):
    print(index)
    print(f"x={xlist[index]} y={ylist[index]}")	

for index in range(len(xlist)):
	goto(xlist[index]/2, ylist[index]/2)

"""

"""
x = 100
y = 200
goto(x, y) # x=100 y=200

x = x - 200
goto(x, y) # x=-100 y=200

y = y - 400
goto(x, y) # x=-100 y=-200

x = x + 200
goto(x, y) # x=100 y=-200

y = y + 400
goto(x, y) # x=100 y=200
"""

"""
# 数値リテラル
print(10)
print(0.1)

# 文字列リテラル
print("ABC")
print("あいう")

# 算術演算子
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 % 2)
print(3 ** 2)

# 文字列の連結
print("abc" + "def")

# 文字列の繰り返し
print(3 * "abc")

# 数値リテラルを変数x,yに代入
x = 100
y = 200
print(x)
print(y)

x = x + 100
y = y * 2
print(x) # -> 200
print(y) # -> 400

# f文字列
print(f"x={x} y={y}") # -> x=200 y=400
"""
