from adventurer import Adventurer

missions = [
    {"coor": (5, 5), "finding": "Shard", "found": False},
    {"coor": (10, -2), "finding": "Compass", "found": False},
    {"coor": (-7, 4), "finding": "Animal Bones", "found": False},
    {"coor": (3, 8), "finding": "Silver Key", "found": False},
    {"coor": (-9, -9), "finding": "Golden Idol", "found": False, "requirement": "Silver Key"}
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
        requirement = mission.get("requirement", None)

        if requirement is not None and not any(item == requirement for item in adventurer.inventory):
            print(f"Require: {requirement}.")
            return

        if not hasfound and ax == rx and ay == ry:
            print(f"You found {finding}!")
            foundSomething = True
            mission["found"] = True
            adventurer.inventory.append(finding)
            return
        
    if not foundSomething:
        print(f"You got nothing.")

def check_mission():
    return all(mission.get("found") for mission in missions)

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
    
    if check_mission():
        print("*** Mission Complete! ***")
        isRunning = False