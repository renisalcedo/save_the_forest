from Character import Character

class Player(Character):
    def __init__(self, weapon, fight = False):
        Character.__init__(self, status, level, name)
        self.weapon = weapon
        self.fight = fight 

    def shoot(self):
        ##shoots projectile
        atk = self.get_stat('atk')

        return atk 


    def defend(self, fight):
        #reflect damage from the attacker 
        if fight == False:
            dfnd = self.get_stat('dfnd')
            dmg = 
        else:
            print()


    def set_prop(key, val):
    #Updates key property of player with a given value
    #upgrade: Level 5 is the max level of upgrade. 
    #Level by 1 and set the property depending on the character.
