WIDTH = 640
HEIGHT = 480

"""
dic = {"a": "apple", "b": "banana", "c": "cherry"}
print(dic)

print(dic["a"])
print(dic["b"])
print(dic["c"])

for key in dic:
    print(dic[key])

x = "b"

if x == "a":
    print("apple")
elif x == "b":
    print("banana")
elif x == "c":
    print("cherry")

print(dic[x])

"""

map_dic = {
    "f": "tile0",  # 森
    "s": "tile1",  # 海
    "r": "tile2",  # 道路
    "g": "tile3",  # 草
}

map_data = [
    ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
    ["f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f"],
    ["f", "f", "g", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g", "f", "f", "f", "f"],
    ["f", "f", "f", "f", "f", "g", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g", "f"],
    ["g", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g", "f", "f", "f", "f", "f", "f", "f", "f"],
    ["f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f"],
    ["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"],
    ["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"],
    ["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"],
    ["f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f"],
    ["g", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g", "f", "f"],
    ["f", "f", "g", "f", "f", "f", "f", "f", "g", "f", "f", "g", "f", "f", "g", "f", "f", "f", "f", "f"],
    ["f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g", "f"],
    ["f", "f", "f", "f", "f", "g", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f"],
    ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
]


class Map:
    def __init__(self, map_dic, map_data, tile_size):
        self.map_dic = map_dic
        self.map_data = map_data
        self.tile_size = tile_size

    def draw(self):
        max_i = WIDTH // self.tile_size
        max_j = HEIGHT // self.tile_size

        for i in range(max_i):
            for j in range(max_j):
                number = self.map_data[j][i]
                image = self.map_dic[number]
                screen.blit(image, (i * self.tile_size, j * self.tile_size))

    def shift(self):
        for list in self.map_data:
            head = list.pop(0)
            list.append(head)

    def shift_reverse(self):
        for list in self.map_data:
            tail = list.pop(len(list)-1)
            list.insert(0, tail)

map = Map(map_dic, map_data, 32)
clock.schedule_interval(map.shift_reverse, 0.2)

car = Actor("car", center=(WIDTH/2, HEIGHT/2))
car.angle = 90

def draw():
    screen.fill("white")
    map.draw()
    car.draw()

def update():
    if keyboard.up:
        car.y += -1
    elif keyboard.down:
        car.y += 1
