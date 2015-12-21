import json

def get_blocks():
    locations = []
    #ret = None
    with open("game.json","r") as f:
        jsontext = f.read()
        #print (jsontext)
        d = json.loads(jsontext)
        blocks = (d["block"])
    for x in blocks:
        locations.append(Block(**x))
    return locations 

class Block():
    def __init__(self,id = "",name = "A room", description = "an empty room", neighbours = {},items={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbours = neighbours
        self.items = items
    def _neighbour(self,direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None
    def _item(self,item):
        if item in self.items:
            return self.items[item]
        else:
            return None
    def removeItem(self,item):
        #remove the itemm from the import dictionary
        self.items.pop(item, None)
    def returnItems(self):
        #return a list of items in the room
        return list(self.items.keys())
#get_blocks()

