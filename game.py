from adventurer import Adventurer

missions = [
    {"coor": (5, 5), "finding": "Shard", "found": False},
    {"coor": (10, -2), "finding": "Compass", "found": False},
    {"coor": (10, -2), "finding": "Ancient Map", "found": False},
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

        if not hasfound and ax == rx and ay == ry:
            if requirement and requirement not in adventurer.inventory:
                print(f"Require: {requirement}.")
                foundSomething = True
                continue

            print(f"You found {finding}!")
            foundSomething = True
            mission["found"] = True
            adventurer.inventory.append(finding)
        
    if not foundSomething:
        print(f"You got nothing.")

def check_map():
    ax, ay = adventurer.getPos()
    for y in range(ay - 4, ay + 5):
        for x in range(ax - 4, ax + 5):
            if (x, y) in [mission.get("coor") for mission in missions if not mission.get("found")]:
                print("@", end=" ")
            elif (x, y) in [mission.get("coor") for mission in missions if mission.get("found")]:
                print("v", end=" ")
            else:
                print("-", end=" ")
        print()

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
        case "t":
            check_map()
        case "p":
            isRunning = False
    
    if check_mission():
        print("*** Mission Complete! ***")
        isRunning = False