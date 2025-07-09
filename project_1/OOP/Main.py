from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

def battle(e1:Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('---------')
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} health: {e1.health_points}")
        print(f"{e2.get_type_of_enemy()} health: {e2.health_points}")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('-----------')
    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins !")
    else:
        print(f"{e2.get_type_of_enemy()} wins !")

def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print('---------')
        print(f"Hero health: {hero.health_points}")
        print(f"{enemy.get_type_of_enemy()} health: {enemy.health_points}")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

        enemy.special_attack()

    print('-----------')
    if hero.health_points > 0:
        print(f"Hero wins !")
    else:
        print(f"{enemy.get_type_of_enemy()} wins !")

zombie = Zombie(10,1)
ogre = Ogre(30, 10)

hero = Hero(10,2)

weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)
hero_battle(hero, zombie)