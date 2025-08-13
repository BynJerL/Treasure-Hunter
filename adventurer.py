class Adventurer:
    def __init__(self, name: str, speed: int, initX: int = 0, initY: int = 0):
        self.name = name
        self.speed = speed
        self.posX = initX
        self.posY = initY
    
    def goToPos(self, x: int, y: int):
        self.posX = x
        self.posY = y
    
    def goWest(self):
        self.posX -= self.speed
    
    def goEast(self):
        self.posX += self.speed
    
    def goNorth(self):
        self.posY -= self.speed

    def goSouth(self):
        self.posY += self.speed