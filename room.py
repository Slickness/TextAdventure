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
    def __init__(self,id = "",name = "A room", description = "an empty room", neighbours = {}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbours = neighbours
    def _neighbour(self,direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None
#get_blocks()

