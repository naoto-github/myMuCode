import numpy as np

WIDTH = 640
HEIGHT = 480

map_dic = {
    0: "tile0",  # 森
    1: "tile1",  # 海
    2: "tile2",  # 道路
}

class Map:
    def __init__(self, map_file, map_dic):

        self.map_data = np.zeros((8, 10))
        self.map_dic = map_dic

        with open(map_file) as file:
            for i, line in enumerate(file):
                for j, number in enumerate(line.strip()):
                    print(f"{i} {j}")
                    self.map_data[i][j] = number

    def draw(self):

        for i in range(8):
            for j in range(10):
                x = 64 * j
                y = 64 * i
                number = self.map_data[i][j]
                image = self.map_dic[number]
                screen.blit(image, (x, y))


map = Map("map.txt", map_dic)

def draw():
    screen.fill("white")
    map.draw()
