import json
# This class is for all the enemies in the gaem


def get_enemy():
    enemies = []
    with open("game.json", "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        enemy = (d["enemy"])
        for x in enemy:
            enemies.append(Enemy(**x))
        return enemies


class Enemy():
    def __init__(self, name="default", hp=1, attack=1, points=10):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.points = points

    def isDead(self):
        return self.hp <= 0

    def updateHp(self, value):
        self.hp -= value
