from adventurer import Adventurer

missions = [
    {"coor": (5, 5), "finding": "Shard", "found": False},
    {"coor": (10, -2), "finding": "Compass", "found": False},
    {"coor": (-7, 4), "finding": "Animal Bones", "found": False}
]

adventurer = Adventurer("Echo")
isRunning = True

def excavate():
    print("Surveying the area...")
    foundSomething = False

    for mission in missions:
        rx, ry = mission.get("coor")
        ax, ay = adventurer.getPos()
        finding = mission.get("finding", "nothing")
        hasfound = mission.get("found")

        if not hasfound and ax == rx and ay == ry:
            print(f"You found {finding}!")
            foundSomething = True
            mission["found"] = True
            adventurer.inventory.append(finding)
        
    if not foundSomething:
        print(f"You got nothing.")

while isRunning:
    adventurer.printPos()

    action = input("Your Action: ")

    match action:
        case "w":
            adventurer.goNorth()
        case "a":
            adventurer.goWest()
        case "s":
            adventurer.goSouth()
        case "d":
            adventurer.goEast()
        case "g":
            excavate()
        case "h":
            adventurer.showInventory()
        case "p":
            isRunning = False