from Enemy import *
import random

class Ogre(Enemy):
    def __init__(self, health_points=10, attack_damage=1):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Ogre talking")

    def special_attack(self):
        did_attack_work = random.random() < 0.2
        if did_attack_work:
            self.health_points += 4
            print("Ogre regenerated 4 HP")