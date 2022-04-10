WIDTH = 640 # ウィンドウの幅
HEIGHT = 480 # ウィンドウの高さ

def draw():
    # 背景色が白のスクリーン
    screen.fill("white")

    # 始点(50, 50)から終点(200, 50)に黒色の直線を描く
    screen.draw.line((50, 50), (200, 50), "black")

    # 左上の座標(50, 150)，幅100，高さ100の赤色の正方形を描く
    screen.draw.rect(Rect((50, 150), (100, 100)), "red")

    # 左上の座標(50, 300)，幅100，高さ100，緑色の塗りつぶしの正方形を描く
    screen.draw.filled_rect(Rect((50, 300), (100, 100)), "green")

    # 中心(300, 150)，半径50，青色の正方形を描く
    screen.draw.circle((300, 150), 50, "blue")

    # 中心(300, 300)，半径50，黄色の塗りつぶしの正方形を描く
    screen.draw.filled_circle((300, 300), 50, "yellow")

    # 左上の座標(400, 150)，フォントサイズ24，黒色の文字列「ABC」を描く
    screen.draw.text("ABC", (400, 150), color="black")

    # 左上の座標(400, 300)，フォントサイズ32，黒色の文字列「あいう」を描く
    # IPAexフォント https://moji.or.jp/ipafont/
    screen.draw.text("あいう", (400, 300), fontname="ipaexg", color="black", fontsize=32)
