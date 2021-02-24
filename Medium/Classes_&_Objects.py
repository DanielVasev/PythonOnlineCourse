class Enemy:
    life = 5

    def attack(self):
        if self.life <= 0:
            print("Enemy is dead.. you cant attack it...")
        else:
            print("Ouch!")
            self.life -= 1

    def check(self):
        if self.life <= 0:
            print("Im dead!")

        else:
            print(str(self.life) + "life left!")


enemy1 = Enemy()
enemy1.check()
enemy1.attack()
enemy1.check()

