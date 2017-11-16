class Counter_Strike():      #First Parent Method
    def kill(self):
        print("I can now kill the terrorists")


class Counter_Strike2():   #Second Parent Method
    def diffuse(self):
        print("I am diffusing the bomb")


class Game(Counter_Strike , Counter_Strike2):    # Class Game inherits Multiple Classes.
    pass


cs = Game()
cs.diffuse()
cs.kill()