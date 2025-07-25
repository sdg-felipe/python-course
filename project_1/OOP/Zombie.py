from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points = 10, attack_damage = 1):
        super().__init__(type_of_enemy = 'Zombie', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Grumbling")

    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_attack(self):
        did_attack_work = random.random() < 0.5
        if did_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP")