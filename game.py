from adventurer import Adventurer

mission = [
    {"coor": (5, 5), "finding": "Shard", "found": False},
    {"coor": (10, -2), "finding": "Compass", "found": False},
    {"coor": (-7, 4), "finding": "Animal Bones", "found": False}
]

adventurer = Adventurer("Echo")

isRunning = True

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