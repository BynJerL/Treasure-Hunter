class Adventurer:
    def __init__(self, name: str, speed: int = 1, initX: int = 0, initY: int = 0, inventory: list = None):
        self.name = name
        self.speed = speed
        self.posX = initX
        self.posY = initY
        self.inventory = inventory or []
    
    def printPos(self):
        print(f"{self.name}: (x={self.posX}, y={self.posY})")
    
    def getPos(self):
        return (self.posX, self.posY)

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
    
    def showInventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")