class Mario():
    def move(self):
        print("Im moving")

class Shroom():
    def eat_shroom(self):
        print("Now im big!")

class BigMario(Mario, Shroom):
    pass


daniel = BigMario()
daniel.move()
daniel.eat_shroom()
