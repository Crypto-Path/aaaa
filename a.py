import time
import random

class Player():
    def __init__(self, name, inventory):
        self.name = name
        self.position = [random.randint(-10, 10), random.randint(-10, 10)]
        self.inventory = inventory
        
    def addItem(self, itemName):
        self.inventory.append(itemName)
        
    def hasItem(self, itemName):
        ret = False
        for x in self.inventory:
            if (x == itemName):
                ret = True
        return ret
            
    def removeItem(self, itemName):
        self.inventory.remove(itemName)
            
    
items = [
]

harvest = [
    "Apple",
    "Stick"
]

tools = [
    "Axe",
    "Pick",
    "Sword"
]

chopping = [
    "log"
]

mining = [
    "rock"
]

for x in harvest:
    items.append(x)
    
for x in tools:
    items.append(x)
    
for x in chopping:
    items.append(x)
    
for x in mining:
    items.append(x)

players = [
    Player("Jim", []),
    Player("Bob", []),
    Player("Willow", []),
    Player("Willard", []),
    Player("Jeniffer", []),
    Player("Jerry", []),
    Player("Billy", []),
    Player("Renfroe", []),
    Player("Lil Billy", []),
    Player("Drauss", [])
]

def findItem(table, player):
    item = random.choice(table)
    player.addItem(item)
    return item

while(True):
    time.sleep(1)
    for player in players:
        player.position[0] += random.randint(0,2)-1
        player.position[1] += random.randint(0,2)-1
        
        if (player.position[0] > 10):
            player.position[0] = 10
        if (player.position[0] < -10):
            player.position[0] = -10
        if (player.position[1] > 10):
            player.position[1] = 10
        if (player.position[1] < -10):
            player.position[1] = -10
            
        collided = False
        for otherPlayer in players:
            if (otherPlayer != player):
                if (player.position == otherPlayer.position):
                    collided = True
                    
                    r = random.choice(["Nothing", "Chat", "Fight", "Trade"])
                    match (r):
                        case "Chat":
                            print(player.name + " chatted with " + otherPlayer.name)
                        case "Fight":
                            print(player.name + " got in a fight with " + otherPlayer.name)
                        case "Trade":
                            lookingFor1 = random.choice(items)
                            lookingFor2 = random.choice(items)
                            if (otherPlayer.hasItem(lookingFor1)):
                                if (player.hasItem(lookingFor2)):
                                    print(player.name + " traded " + lookingFor2 + " for " + lookingFor1 + " with " + otherPlayer.name)
                                    player.removeItem(lookingFor2)
                                    player.addItem(lookingFor1)
                                    otherPlayer.removeItem(lookingFor1)
                                    otherPlayer.addItem(lookingFor2)
                       
        if (collided == False):
            r = random.choice(["Search", "Chop", "Mine", "Hunt", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing",  "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing",  "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing",  "Nothing"])
            match (r):
                case "Search":
                    if (not player.hasItem("Pick")):
                        if (not player.hasItem("Axe")):
                            if (not player.hasItem("Sword")):
                                item = findItem(tools, player)
                                print(player.name + " found a tool, " + item)
                                break
                    item = findItem(harvest, player)
                    print(player.name + " found item, " + item)
                case "Chop":
                    if (player.hasItem("Axe")):
                        item = findItem(chopping, player)
                        print(player.name + " chopped a tree for a " + item)
                case "Mine":
                    if (player.hasItem("Pick")):
                        item = findItem(mining, player)
                        print(player.name + " went mining for a " + item)
                    